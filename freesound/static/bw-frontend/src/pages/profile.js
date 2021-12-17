import {makeSoundsMap} from '../components/mapsMapbox';
import {handleGenericModal, handleModal} from "../components/modal";

// Latest sounds/Latest tags taps

const taps = [...document.querySelectorAll('[data-toggle="tap"]')];
const tapsElements = document.getElementsByClassName('bw-profile__tap_container');

const cleanActiveClass = () => {
  taps.forEach(tap => tap.classList.remove('active'));
  tapsElements.forEach(tapElement =>
      tapElement.classList.remove('bw-profile__tap_container__active')
  );
};

const handleTap = tap => {
  cleanActiveClass();

  const tapContainer = document.getElementById(tap.dataset.target.substring(1));

  tap.classList.add('active');
  tapContainer.classList.add('bw-profile__tap_container__active');
};

taps.forEach(tap => {
  tap.addEventListener('click', () => handleTap(tap));
});

// Follow modals
const userFollowersButton = document.getElementById('user-followers-button');
const userFollowUsersButton = document.getElementById('user-following-users-button');
const userFollowTagsButton = document.getElementById('user-following-tags-button');

const removeFollowModalUrlParams = () => {
  const searchParams = new URLSearchParams(window.location.search);
  [userFollowersButton, userFollowUsersButton, userFollowTagsButton].forEach(button => {
    searchParams.delete(button.dataset.modalActivationParam);
  });
  const url = window.location.protocol + '//' + window.location.host + window.location.pathname + '?' + searchParams.toString();
  window.history.replaceState(null, "", url);
};

const setFollowModalUrlParamToCurrentPage = (modalActivationParam) => {
  const searchParams = new URLSearchParams(window.location.search);

  // Find current page from paginator element in loaded modal
  let page = 1;
  const genericModalWrapperElement = document.getElementById('genericModalWrapper');
  genericModalWrapperElement.getElementsByClassName('bw-pagination_selected').forEach(element => {
    page = parseInt(element.innerHTML, 10);
  });
  searchParams.set(modalActivationParam, page);
  const url = window.location.protocol + '//' + window.location.host + window.location.pathname + '?' + searchParams.toString();
  window.history.replaceState(null, "", url);
};

[userFollowersButton, userFollowUsersButton, userFollowTagsButton].forEach(button => {
  button.addEventListener('click', () => {
    handleGenericModal(button.dataset.modalContentUrl, () => {
      setFollowModalUrlParamToCurrentPage(button.dataset.modalActivationParam);
    }, () => {
      removeFollowModalUrlParams();
    });
  });
});

const urlParams = new URLSearchParams(window.location.search);
const followersModalParam = urlParams.get(userFollowersButton.dataset.modalActivationParam);
const followingModalParam = urlParams.get(userFollowUsersButton.dataset.modalActivationParam);
const followingTagsModalParam = urlParams.get(userFollowTagsButton.dataset.modalActivationParam);

if (followersModalParam) {
  handleGenericModal(userFollowersButton.dataset.modalContentUrl, () => {
    setFollowModalUrlParamToCurrentPage(userFollowersButton.dataset.modalActivationParam);
  }, () => {
    removeFollowModalUrlParams();
  });
}

if (followingModalParam) {
  handleGenericModal(userFollowUsersButton.dataset.modalContentUrl, () => {
    setFollowModalUrlParamToCurrentPage(userFollowUsersButton.dataset.modalActivationParam);
  }, () => {
    removeFollowModalUrlParams();
  });
}

if (followingTagsModalParam) {
  handleGenericModal(userFollowTagsButton.dataset.modalContentUrl, () => {
    setFollowModalUrlParamToCurrentPage(userFollowTagsButton.dataset.modalActivationParam);
  }, () => {
    removeFollowModalUrlParams();
  });
}


// User geotags map
// Load the map only when user clicks on "load map" button
const mapCanvas = document.getElementById('map_canvas');
const latestGeotagsSection = document.getElementById('latest_geotags');
const loadButtonWrapper = document.createElement('div');
const loadMapButton = document.createElement('button');
const loadMap = () => {
  loadButtonWrapper.remove();
  if (latestGeotagsSection.getAttribute('data-map-loaded') !== 'true') {
    makeSoundsMap(mapCanvas.dataset.geotagsUrl, 'map_canvas', () => {
      latestGeotagsSection.setAttribute('data-map-loaded', "true");
      latestGeotagsSection.style.display = 'block'; // Once map is ready, show geotags section
    });
  }
}
loadButtonWrapper.id = 'loadMapButtonWrapper';
loadButtonWrapper.classList.add('text-center v-spacing-top-4 v-spacing-bottom-4');
loadMapButton.onclick = () => {loadMap()};
loadMapButton.classList.add('btn-inverted');
loadMapButton.innerText = 'Load map...';
loadButtonWrapper.appendChild(loadMapButton);
latestGeotagsSection.parentNode.insertBefore(loadButtonWrapper, latestGeotagsSection);
