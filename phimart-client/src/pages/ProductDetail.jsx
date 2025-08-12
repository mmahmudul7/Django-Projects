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
        <div className="w-3/4 mx-auto px-4 py-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12">
                <ProductImageGallery
                    images={product.images}
                    ProductName={product.name}
                />
                <div className="mt-auto">
                    <AddToCartButton product={product} />
                </div>
            </div>
        </div>
    );
};

export default ProductDetail;
