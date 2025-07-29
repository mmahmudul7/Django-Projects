import { useEffect } from 'react';
import axios from 'axios';

const Product = () => {
    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/v1/products/')
            .then((res) => console.log(res.data.results));
    }, []);
    return <div></div>;
};

export default Product;
