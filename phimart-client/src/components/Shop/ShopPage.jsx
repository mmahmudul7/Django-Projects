import { useState } from 'react';
import ProductList from './ProductList';
import Pagination from './Pagination';
import useFetchProducts from '../../hooks/useFetchProducts';
import FilterSection from './FilterSection';

const ShopPage = () => {
    const [currentPage, setCurrentPage] = useState(1);
    const { products, loading, totalPages } = useFetchProducts(currentPage);

    return (
        <div>
            <FilterSection />
            <ProductList products={products} loading={loading} />
            <Pagination
                totalPages={totalPages}
                currentPage={currentPage}
                handlePageChange={setCurrentPage}
            />
        </div>
    );
};

export default ShopPage;
