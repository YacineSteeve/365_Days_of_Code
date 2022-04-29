const main = document.querySelector('main');
const filterButton = document.querySelector('button');
const categorySelector = document.querySelector('select');
let products;


function fetchBlobAndShow(product) {
    const url = `images/${product.image}`;

    fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`${response.status}`);
            }
            return response.blob()
        })
        .then((blob) => showProduct(product, blob))
        .catch(error => console.error(`Image fetch failed! ${error}`));
}

/**
 * Create a section for the product in main and fill it.
 * @param product {Object}       - The product
 * @param productBlob {Blob}     - A blob object containing a reference to the product's image.
 * @param product.name {String}
 * @param product.price {Number}
 * @param product.image {String}
 * @param product.type {String}
 */
function showProduct(product, productBlob) {
    const productSection = document.createElement('section');
    const productName = document.createElement('h2');
    const productPrice = document.createElement('p');
    const productImage = document.createElement('img');

    productName.textContent = product.name.charAt(0).toUpperCase() + product.name.slice(1,);
    productPrice.textContent = `$${product.price.toFixed(2)}`;
    productImage.src = URL.createObjectURL(productBlob);
    productImage.alt = product.name;

    productSection.appendChild(productName);
    productSection.appendChild(productPrice);
    productSection.appendChild(productImage);

    productSection.setAttribute('class', product.type);

    main.appendChild(productSection);
}

fetch('products.json')
    .then((response) => {
        if (!response.ok) {
            throw new Error(`${response.status}`);
        }
        return response.json()
    })
    .then(json => {
        products = json;
        products.forEach((product) => { fetchBlobAndShow(product) });
    })
    .catch(error => console.error(`Fetch failed! ${error}`));


filterButton.addEventListener('click', () => {
    const currentChildren = document.querySelectorAll('main section');
    
    if (categorySelector.value !== 'All') {
        for (const child of currentChildren) {
            main.removeChild(child);
        }
        
        for (const product of products) {
            if (product.type === categorySelector.value.toLowerCase()) {
                fetchBlobAndShow(product);
            }
        }
    } else if (currentChildren.length !== products.length) {
        for (const child of currentChildren) {
            main.removeChild(child);
        }
        
        products.forEach((product) => { fetchBlobAndShow(product) });
    }
})
