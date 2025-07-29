import defaultImage from '../../assets/default_product.webp';

const ProductItem = ({ product }) => {
    return (
        <div className="card bg-base-100 w-96 shadow-sm">
            <figure className="px-10 pt-10">
                <img
                    src={
                        product.images.length > 0
                            ? product.images[0].image
                            : defaultImage
                    }
                    alt="Image"
                    className="rounded-xl"
                />
            </figure>
            <div className="card-body items-center text-center">
                <h2 className="card-title">{product.name}</h2>
                <h3 className="font-bold text-xl text-pink-500">
                    ${product.price}
                </h3>
                <p>{product.description}</p>
                <div className="card-actions mt-1">
                    <button className="btn btn-secondary">Buy Now</button>
                </div>
            </div>
        </div>
    );
};

export default ProductItem;
