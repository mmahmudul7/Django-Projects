import { useEffect, useState } from 'react';
import apiClient from '../services/api-client';

const useFetchProducts = (currentPage) => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState([]);
    const [totalPages, setTotalPages] = useState(0);

    useEffect(() => {
        const fetchProducts = async () => {
            setLoading(true);
            try {
                const response = await apiClient.get(
                    `/products/?page=${currentPage}`
                );
                const data = await response.data;

                setProducts(data.results);
                setTotalPages(Math.ceil(data.count / data.results.length));
            } catch (error) {
                console.log(error);
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, [currentPage]);

    return { products, loading, totalPages };
};

export default useFetchProducts;
