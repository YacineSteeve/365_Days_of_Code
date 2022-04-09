function Car(owner, brand, model, year, color, energy) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.color = color;
    this.energy = energy;
    this.owner = {
        ownerName: owner[0],
        ownerSex: owner[1]
    }
}

let myLambo = new Car(['Yacine', 'Male'], 'Lamborghini',
    'Aventador', '2012', 'green', 'fuel');

console.log(myLambo.owner);
