QUEUE_SOUND_MODERATION = 'sound moderation'

TICKET_STATUS_NEW = 'new'
TICKET_STATUS_DEFERRED = 'deferred'
TICKET_STATUS_ACCEPTED = 'accepted'
TICKET_STATUS_CLOSED = 'closed'

MODERATION_TEXTS = [
    (
        'Illegal', "Hey there. Thanks for contributing to Freesound.\n"
        "Unfortunately we've had to delete this sound.\n"
        "\n"
        "Freesound only hosts files that are not copyright infringing. We reject audio taken from copyright "
        "protected media without permission. Please do not upload other people's works. "
        "Only sounds that you have made yourself or own the copyrights.\n"
        "\n"
        "If you'd like to find out what you can upload, please have a look here:\n"
        "https://freesound.org/help/faq/#what-sounds-are-legal-to-put-on-freesound\n"
        "\n"
        "Thanks!"
    ),
    (
        'Music', "Hey there. Thanks for contributing to Freesound.\n"
        "Unfortunately, you've uploaded some music which doesn't fit with the content we allow onto the site. "
        "We do however genrally allow music samples that are under 1 minute long, not songs.\n"
        "\n"
        "Some recommended sites for sharing produced music/songs: "
        "Soundcloud, Bandcamp, CCMixter and The Free Music Archive\n"
        "\n"
        "By the way, we welcome material such as loops, riffs, melodies etc. So you could try cutting up your "
        "music into short instrumental loops and uploading them that way. In fact, music and drum loops "
        "are some of the most searched and downloaded sounds on Freesound!\n"
        "\n"
        "Thanks for understanding!"
    ),
    (
        'Not a Sound', "Hey there. Thanks for contributing to Freesound.\n"
        "\n"
        "You have uploaded a file that does not fit with the type of content Freesound is looking for. "
        "Content we reject includes songs, audiobooks, adverts/commercials, podcasts and copyrighted "
        "material.\n"
        "\n"
        "Thanks for understanding!"
    ),
    (
        'Language', "Hey there. Thanks for contributing to Freesound.\n"
        "This is a great sound, but could you possibly add an English title, description and tags?\n"
        "\n"
        "You can keep your original description, just add the english in too. This will ensure that your "
        "sounds are discoverable in the search. Because our user-base is mainly English speaking, it makes "
        "sense to do this.\n"
        "\n"
        "Also, please include as much detail as you can in the description.\n"
        "\n"
        "If you can't find how to edit your sound here's a little visual guide:\n"
        "https://i.imgur.com/s4w2ysv.jpg\n"
        "\n"
        "Many thanks!"
    ),
    (
        'Description/Tags', "Hey there. Thanks for contributing to Freesound.\n"
        "We noticed that your upload is missing a description / tags. "
        "Before approving, Please could you update this to include more detail? "
        "It's important to help other users find your sound in the search.\n"
        "\n"
        "If you need some guidance on describing please see the following FAQ page:\n"
        "https://freesound.org/help/faq/#how-should-i-describe-my-sounds\n"
        "\n"
        "Also, if you can't find how to edit your sound, here's a little visual guide:\n"
        "https://i.imgur.com/s4w2ysv.jpg\n"
        "\n"
        "Thanks!"
    ),
    (
        'Credit Sounds', "Hey there. Thanks for contributing to Freesound.\n"
        "We've noticed that you have used one or more sounds from this site that have the "
        "'Attribution' and/or 'Non-Commercial' license. Other users need to know this, so before we "
        "can approve it onto the site, we need you to credit these sounds so that everyone can follow "
        "the respective license terms.\n"
        "\n"
        "Here is an example of crediting sounds within your description:\n"
        "https://freesound.org/s/544453\n"
        "\n"
        "If you can't find how to edit your sound, here's a little visual guide:\n"
        "https://i.imgur.com/s4w2ysv.jpg\n"
        "\n"
        "Many thanks!"
    ),
    (
        'Verify Details', "Hey there. Thanks for contributing to Freesound.\n"
        "\n"
        "Before we can moderate your upload, could you possibly update the description/tags? "
        "Any details such as how it was created, recording device, software used, date/location etc- "
        "-are extremely useful.\n"
        "\n"
        "If you can't find how to edit your sound, here's a little visual guide:\n"
        "https://i.imgur.com/s4w2ysv.jpg\n"
        "\n"
        "Many thanks!\n"
        "\n"
        "(If there is no response to this ticket within 2 weeks, the sound will be removed)"
    ),
    (
        'License Mismatch', "Hey there. Thanks for sharing your work on Freesound.\n"
        "We noticed that the sound you've edited/remixed and uploaded doesn't match the original CC "
        "license. This is really important to get correct.\n"
        "\n"
        "Could you please update the license type of the sound by clicking on "
        "'edit sound information' on the sound's page?\n"
        "\n"
        "Many thanks!"
    ),
    (
        'Permission', "Hey there. Thanks for contributing to Freesound.\n"
        "Please could you clarify for us that you have permission to upload the recording of the "
        "performer, singer or speaker to Freesound?\n"
        "\n"
        "It's important that you don't share things that you don't have permission to upload.\n"
        "Please let us know.\n"
        "\n"
        "Thanks!"
    ),
    (
        'Timeout', "Deleting due to the lack of response to the ticket.\n"
        "If you believe this was in error, or you didn't have time to respond, "
        "do feel free to re-upload the sound or get in touch with us.\n"
        "\n"
        "Thanks for understanding!"
    )
]
