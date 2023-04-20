function noDigits(event) {
  if ("1234567890-=_+`~!@#$%^&*()?/|><,.:;'№".indexOf(event.key) != -1)
    event.preventDefault();
}
