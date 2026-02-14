---
name: Song request
description: Suggest a song to add to the game
labels: ['song request']
body:
  - type: input
    id: url
    attributes:
      label: SoundCloud URL
      placeholder: https://soundcloud.com/artist/track
    validations:
      required: true
  - type: input
    id: answer
    attributes:
      label: Display text (answer)
      placeholder: ARTIST - Track Title
    validations:
      required: true
  - type: textarea
    id: notes
    attributes:
      label: Notes
      description: Optional context or alternatives.
    validations:
      required: false
---
