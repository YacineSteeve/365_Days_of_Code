class Person {
    constructor (first, last, age, gender, interests) {
        this.name = {
            first,
            last
        }
        this.age = age
        this.gender = gender
        this.interests = interests
    }

    bio = function () {
        let string = this.name.first + ' ' + this.name.last + ' is ' + this.age + ' years old. '
        let pronoun

        if (this.gender === 'male' || this.gender === 'Male' || this.gender === 'm' || this.gender === 'M') {
            pronoun = 'He likes '
        } else if (this.gender === 'female' || this.gender === 'Female' || this.gender === 'f' || this.gender === 'F') {
            pronoun = 'She likes '
        } else {
            pronoun = 'They like '
        }

        string += pronoun

        if (this.interests.length === 1) {
            string += this.interests[0] + '.'
        } else if (this.interests.length === 2) {
            string += this.interests[0] + ' and ' + this.interests[1] + '.'
        } else {
            for (let i = 0; i < this.interests.length; i++) {
                if (i === this.interests.length - 1) {
                    string += 'and ' + this.interests[i] + '.'
                } else {
                    string += this.interests[i] + ', '
                }
            }
        }

        console.log(string)
    }

    greeting = function () {
        console.log('Hi! I\'m ' + this.name.first + '.')
    }

    farewell = function () {
        console.log(this.name.first + ' has left the building. Bye for now!')
    }
}

class Teacher extends Person {
    constructor(first, last, age, gender, interests, subject) {
        super(first, last, age, gender, interests)
        this.subject = subject
    }

    greeting = function () {
        (this.gender === 'male' || this.gender === 'Male' || this.gender === 'm' || this.gender === 'M')
            ? console.log(`Hello! I'm Mr ${this.name.first} ${this.name.last} and I'm the ${this.subject} teacher.`)
            : console.log(`Hello! I'm Mrs ${this.name.first} ${this.name.last} and I'm the ${this.subject} teacher.`)
    }
}

const person1 = new Person('Tammi', 'Smith', 17, 'female', ['music', 'skiing', 'kickboxing'])
const teacher1 = new Teacher('Duncan', 'McLeon', 46, 'm', ['golf', 'bike'], 'Physics')

console.log(Person)
console.log()
console.log(person1)
console.log()
person1.bio()
console.log()
person1.greeting()
console.log()
person1.farewell()

console.log()
console.log(Teacher)
console.log()
console.log(teacher1)
console.log()
teacher1.bio()
console.log()
teacher1.greeting()
console.log()
teacher1.farewell()
