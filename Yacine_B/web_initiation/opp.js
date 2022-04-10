function Personne(prenom, famille, age, genre, interets) {
    this.nom = {
        'prenom': prenom,
        'famille' : famille
    };
    this.age = age;
    this.genre = genre;
    this.interets = interets;
    this.bio = function() {
        let string = this.nom.prenom + ' ' + this.nom.famille + ' a ' + this.age + ' ans. ';
        let pronom;

        if (this.genre === 'homme' || this.gender === 'Homme' || this.gender === 'h' || this.gender === 'H') {
            pronom = 'Il aime ';
        }
        else if (this.genre === 'femme' || this.gender === 'Femme' || this.gender === 'f' || this.gender === 'F') {
            pronom = 'Elle aime ';
        }
        else {
            pronom = this.nom.prenom + ' aime ';
        }
        string += pronom;

        if (this.interets.length === 1) {
            string += this.interets[0] + '.';
        }
        else if (this.interets.length === 2) {
            string += this.interets[0] + ' et ' + this.interets[1] + '.';
        }
        else {
            for (let i = 0; i < this.interets.length; i++) {
                if (i === this.interets.length - 1) {
                    string += 'et ' + this.interets[i] + '.';
                }
                else {
                    string += this.interets[i] + ', ';
                }
            }
        }

        alert(string);
    };
    this.salutation = function() {
        alert('Bonjour ! Je m\'appelle ' + this.nom.prenom + '.');
    };
};

let personne1 = new Personne('Jean', 'Biche', 32, 'neutre', ['musique', 'tricot', 'boxe']);

console.log(personne1.prototype);
