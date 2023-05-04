#
# Freesound is (c) MUSIC TECHNOLOGY GROUP, UNIVERSITAT POMPEU FABRA
#
# Freesound is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Freesound is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     See AUTHORS file.
#


from django import template
from django.conf import settings

from accounts.models import Profile
from sounds.models import Sound

register = template.Library()


@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound(context, sound, player_size='small', show_bookmark=None, show_similar_sounds=None):
    """This templatetag is used to display a sound with its player. It prepares some variables that are then passed
    to the display_sound.html template to show sound information together with the player.

    Args:
        context (django.template.Context): an object with contextual information for rendering a template. This
          argument is automatically added by Django when calling the templatetag inside a template.
        sound (int or Sound): sound ID or Sound object of the sound that will be shown. If no sound exists for the
          given ID, the display_sound.html will be rendered with empty HTML.
        player_size (str, optional): size of the player to display. This parameter only applies to BW interface.
          See functions below and template file for available sizes. Information about the contents of each
          size is given in the display_sound.html template code.
        show_bookmark (bool, optional): whether or not to show the bookmark button (BW frontend only). If set to None
          it will be decided based on player size and other properties.
        show_similar_sounds (bool, optional): whether or not to show the similar sounds button (BW frontend only). If set to None
          it will be decided based on player size and other properties.

    Returns:
        dict: dictionary with the variables needed for rendering the sound with the display_sound.html template

    """

    def get_sound_using_bulk_query_id(sound_id):
        """Get a sound from the DB using the Sound.objects.bulk_query_id method which returns a Sound object with
        some extra properties loaded.

        Args:
            sound_id (int): ID of the sound to retrieve.

        Returns:
            Sound: sound object with extra loaded properties or None if the sound does not exist or the ID is not valid.

        """
        try:
            return Sound.objects.bulk_query_id([int(sound_id)])[0]
        except ValueError:
            # 'sound' is not an integer
            return None
        except IndexError:
            # No sound with given ID exists (Sound.objects.bulk_query_id returns empty qs)
            return None

    def sound_object_retrieved_using_bulk_query_id(sound):
        """Checeks whether the given Sound object has the extra properties that are loaded if the object was
        retrieved usnig the Sound.objects.bulk_query_id method. Sound objects retrieved with bulk_query_id have
        the following extra properties required in the display_sound templatetag: 'tag_array', 'username',
        'license_name'. To optimize the code, we only check for the presence of 'tag_array' and assume the other
        properties will go together.

        Args:
            sound (Sound): Sound object

        Returns:
            bool: True if the object was retrieved using bulk query ID.

        """
        return hasattr(sound, 'tag_array')
    
    if isinstance(sound, Sound):
        if sound_object_retrieved_using_bulk_query_id(sound):
            sound_obj = sound
        else:
            # If 'sound' is a Sound instance but has not been retrieved using bulk_query_id, we would need to make
            # some extra DB queries to get the metadata that must be rendered. Instead, we retreive again
            # the sound using the bulk_query_id method which will get all needed maetadaata in only one query.
            # Note that we don't re-retrieve when player size contains "no_info" as in these cases there is
            # no extra metadata needed to be shown.
            if 'no_info' not in player_size:
                sound_obj = get_sound_using_bulk_query_id(sound.id)
            else:
                sound_obj = sound
    else:
        # If 'sound' argument is not a Sound instance then we assume it is a sound ID and we retreive the
        # corresponding object from the DB.
        sound_obj = get_sound_using_bulk_query_id(sound)

    if sound_obj is None:
        return {
            'sound': None,
        }
    else:
        request = context['request']
        return {
            'sound': sound_obj,
            'user_profile_locations': Profile.locations_static(sound_obj.user_id, getattr(sound_obj, 'user_has_avatar', False)),
            'media_url': context['media_url'],
            'request': request,
            'is_explicit': sound_obj.is_explicit and
                           (not request.user.is_authenticated or not request.user.profile.is_adult),
            'is_authenticated': request.user.is_authenticated,
            'show_bookmark_button': show_bookmark if show_bookmark is not None else (player_size == 'small' or player_size == 'small_no_info' or player_size == 'big_no_info'),  # Only BW
            'show_similar_sounds_button': show_similar_sounds if show_similar_sounds is not None else (player_size == 'small' or player_size == 'small_no_info' or player_size == 'big_no_info'),  # Only BW
            'request_user_is_author': request.user.is_authenticated and sound_obj.user_id == request.user.id,
            'player_size': player_size,
            'show_milliseconds': 'true' if (player_size == 'big_no_info' or sound_obj.duration < 10) else 'false',  # Only BW
            'min_num_ratings': settings.MIN_NUMBER_RATINGS,
        }


@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_small(context, sound):
    return display_sound(context, sound, player_size='small')

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_small_no_bookmark(context, sound):
    return display_sound(context, sound, player_size='small', show_bookmark=False, show_similar_sounds=False)

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_middle(context, sound):
    return display_sound(context, sound, player_size='middle', show_bookmark=True, show_similar_sounds=True)

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_big_no_info(context, sound):
    return display_sound(context, sound, player_size='big_no_info')

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_big_no_info_no_bookmark(context, sound):
    return display_sound(context, sound, player_size='big_no_info', show_bookmark=False, show_similar_sounds=False)

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_small_no_info(context, sound):
    return display_sound(context, sound, player_size='small_no_info')

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_minimal(context, sound):
    return display_sound(context, sound, player_size='minimal')

@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_no_sound_object(context, file_data, player_size):
    '''
    This player works for sounds which have no Sound object. It requires
    URLs to the sound files (mp3 and ogg)a and the wave/spectral images, and
    the duration of the sound the JS player can be created. This data is 
    passed through the file_data argument. Here is an example of how file_data 
    should look like if preapring it from a Sound object:
    
    file_data = {
        'duration': sound.duration,
        'samplerate': sound.samplerate,  # Useful for the ruler of the player, if not indicated, a default will be assumed
        'preview_mp3': sound.locations('preview.LQ.mp3.url'),
        'preview_ogg': sound.locations('preview.LQ.ogg.url'),
        'wave': sound.locations('display.wave_bw.L.url'),
        'spectral': sound.locations('display.spectral_bw.L.url'),
        'id': sound.id,  # Only used for sounds that do actually have a sound object so we can display bookmark/similarity buttons
        'username': sound.user.username,  # Only used for sounds that do actually have a sound object so we can display bookmark/similarity buttons
        'similarity_state': sound.similarity_state  # Only used for sounds that do actually have a sound object so we can display bookmark/similarity buttons
    }
    '''
    return {
        'sound': {
            'id': file_data.get('id', file_data['preview_mp3'].split('/')[-2]),  # If no id, use a unique fake ID to avoid caching problems
            'username': file_data.get('username', 'nousername'),
            'similarity_state': file_data.get('similarity_state', 'FA'),
            'duration': file_data['duration'],
            'samplerate': file_data.get('samplerate', 44100),
            'locations': {
                'preview': {
                    'LQ': {
                        'mp3': {'url': file_data['preview_mp3']},
                        'ogg': {'url': file_data['preview_ogg']}
                    }
                },
                'display': {
                    'wave_bw': {
                        'M': {'url': file_data['wave']},
                        'L': {'url': file_data['wave']}
                    }, 
                    'spectral_bw': {
                        'M': {'url': file_data['spectral']},
                        'L': {'url': file_data['spectral']}
                    }
                }
            }
        },
        'show_milliseconds': 'true' if ('big' in player_size ) else 'false',
        'show_bookmark_button': 'id' in file_data,
        'show_similar_sounds_button': 'similarity_state' in file_data,
        'player_size': player_size
    }


@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_big_no_sound_object(context, file_data):
    return display_sound_no_sound_object(context, file_data, player_size='big_no_info')


@register.inclusion_tag('sounds/display_sound.html', takes_context=True)
def display_sound_small_no_sound_object(context, file_data):
    return display_sound_no_sound_object(context, file_data, player_size='small_no_info')
   

@register.inclusion_tag('sounds/display_sound_selectable.html', takes_context=True)
def display_sound_small_selectable(context, sound, selected=False):
    context = context.get('original_context', context)  # This is to allow passing context in nested inclusion tags
    tvars = display_sound_small_no_bookmark(context, sound)
    tvars.update({
        'selected': selected,
    })
    return tvars
