console.log(`Démarrage`);
let image;

fetch('coffee.jpg')
    .then((response) => {
        console.log(`Ça a fonctionné :)`)
        return response.blob();
    })
    .then((myBlob) => {
        let objectURL = URL.createObjectURL(myBlob);
        image = document.createElement('img');
        image.src = objectURL;
        document.body.appendChild(image);
    })
    .catch((error) => {
        console.log(`Il y a eu un problème avec votre opération de récupération : ${error.message}`);
    });

console.log(`C'est fait !`);
