const submitButton = document.getElementById('contact-submit')
const submitted = document.getElementById('submitted')
const input1 = document.getElementById('contact-name')
const input2 = document.getElementById('contact-email')
const input3 = document.getElementById('contact-message')

const inputs = [input1, input2, input3]

submitButton.addEventListener('click', saySmtg)

function saySmtg () {
  let anyEmpty = false

  for (let i = 0; i < 3; i++) {
    if (inputs[i].value === '') {
      anyEmpty = true
    }
  }

  submitted.style.maxWidth = '150px'
  submitted.style.marginTop = '15px'
  submitted.style.marginBottom = '-15px'
  submitted.style.textAlign = 'center'

  if (anyEmpty) {
    submitted.textContent = 'Toutes les informations demandées doivent être mentionnées!'
  } else {
    submitted.textContent = 'Envoyé avec succès! Votre requête sera traitée dans les plus brefs délais.'
  }
}
