const main = document.querySelector('main');
const filterButton = document.querySelector('button');
const categorySelector = document.querySelector('select');
const input = document.querySelector('input');
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

function checkMatching(product, condition) {
    if (condition) {
        fetchBlobAndShow(product);
    }
}

function filterProducts() {

    while (main.firstChild) {
        main.removeChild(main.firstChild);
    }

    products.forEach((product) => {
        const productNameAndType = product.name + ' ' + product.type;

        if (categorySelector.value === 'All' && input.value === '') {
            fetchBlobAndShow(product)
        } else if (categorySelector.value !== 'All' && input.value !== '') {
            checkMatching(product, product.type === categorySelector.value.toLowerCase()
                && productNameAndType.includes(input.value.toLowerCase()));
        } else if (categorySelector.value === 'All' && input.value !== '') {
            checkMatching(product, productNameAndType.includes(input.value.toLowerCase()));
        } else if (categorySelector.value !== 'All' && input.value === '') {
            checkMatching(product, product.type === categorySelector.value.toLowerCase());
        }
    })
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
        products.forEach((product) => {
            fetchBlobAndShow(product)
        });
    })
    .catch(error => console.error(`Fetch failed! ${error}`));

filterButton.addEventListener('click', filterProducts);

input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        filterProducts();
    }
})
