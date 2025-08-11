import { Swiper, SwiperSlide } from 'swiper/react';
import { useState } from 'react';
import { Navigation, Thumbs } from 'swiper/modules';
import defaultImage from '../../assets/default_product.webp';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

const ProductImageGallery = ({ images, ProductName }) => {
    const [thumbsSwiper] = useState(null);
    const displayImages = images.length > 0 ? images : [defaultImage];

    return (
        <div className="rounded-lg border overflow-hidden">
            <Swiper
                modules={[Navigation, Thumbs]}
                navigation
                thumbs={{
                    swiper:
                        thumbsSwiper && !thumbsSwiper.destroyed
                            ? thumbsSwiper
                            : null,
                }}
                className="product-main-slider"
            >
                {displayImages.map((imageObj, index) => (
                    <SwiperSlide key={index}>
                        <img
                            src={imageObj.image}
                            alt={ProductName}
                            className="h-full w-full object-contain"
                        />
                    </SwiperSlide>
                ))}
            </Swiper>
        </div>
    );
};

export default ProductImageGallery;
