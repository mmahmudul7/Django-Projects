import AddToCartButton from '../components/ProductDetails/AddToCartButton';
import ProductImageGallery from '../components/ProductDetails/ProductImageGallery';

const ProductDetail = () => {
    const product = {
        id: 40,
        name: 'Fantasy Novel',
        description: 'High-quality fantasy novel for everyday use.',
        price: 347.72,
        stock: 102,
        category: 4,
        price_with_tax: 382.49,
        images: [
            {
                id: 4,
                image: 'https://res.cloudinary.com/duq4xgaca/image/upload/v1754894675/ef76jiqe3toduay3jplp.webp',
            },
            {
                id: 5,
                image: 'https://res.cloudinary.com/duq4xgaca/image/upload/v1754894691/ewydg8zf4d2kptjb6dql.jpg',
            },
        ],
    };

    return (
        <div>
            <ProductImageGallery
                images={product.images}
                ProductName={product.name}
            />
            <AddToCartButton />
        </div>
    );
};

export default ProductDetail;
