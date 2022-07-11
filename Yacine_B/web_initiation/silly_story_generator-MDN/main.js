const customNameInput = document.querySelector('.name-input')
const unitSystemRadio = document.querySelectorAll('.unit-radio')
const genButton = document.querySelector('.generator-button')

const storyPara = document.querySelector('.story-para')

const rawText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.'

const stringX = ['Willy the Goblin',
  'Big Daddy',
  'Father Christmas']

const stringY = ['the soup kitchen',
  'Disneyland',
  'the White House']

const stringZ = ['spontaneously combusted',
  'melted into a puddle on the sidewalk',
  'turned into a slug and crawled away']

const strings = [stringX, stringY, stringZ]

customNameInput.focus()
storyPara.style.visibility = 'hidden'
genButton.addEventListener('click', displayStory)

function selectRandomStrings () {
  const randomStrings = []

  for (let i = 0; i < strings.length; i++) {
    const index = Math.floor(Math.random() * strings[i].length)
    randomStrings.push(strings[i][index])
  }

  return randomStrings
}

function replaceStrings (storyText) {
  const toReplace = [':insertx:', ':inserty:', ':insertz:']
  const newStrings = selectRandomStrings()
  let newStoryText = storyText

  for (let i = 0; i < toReplace.length; i++) {
    if (i === 0) {
      newStoryText = newStoryText.replace(toReplace[i], newStrings[i])
    }
    newStoryText = newStoryText.replace(toReplace[i], newStrings[i])
  }

  return newStoryText
}

function displayStory () {
  let newStory = rawText
  const customName = customNameInput.value
  let unitSystem

  for (const radio of unitSystemRadio) {
    if (radio.checked) {
      unitSystem = radio.value
      break
    }
  }

  if (customName !== '') {
    newStory = newStory.replace('Bob', customName)
  }

  if (unitSystem === 'uk') {
    newStory = newStory.replace('94 fahrenheit', '34 centigrade')
    newStory = newStory.replace('300 pounds', '21 stone')
  }

  newStory = replaceStrings(newStory)

  storyPara.textContent = newStory

  if (storyPara.style.visibility = 'hidden') {
    storyPara.style.visibility = 'visible'
  }

  customNameInput.focus()
}
