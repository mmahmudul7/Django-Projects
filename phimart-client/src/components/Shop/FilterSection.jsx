const FilterSection = () => {
    return (
        <div className="my-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Price Range  */}
            <div className="bg-white p-4 rounded-lg shadow ">
                <label className="block  text-sm  font-medium text-gray-700 mb-2">
                    Price Range
                </label>
                <div className="flex items-center space-x-4 mb-2">
                    <input
                        type="number"
                        className="w-20 p-2 border rounded-md"
                    />
                    <input type="range" className="w-full" />
                </div>
                <div className="flex items-center space-x-4">
                    <input
                        type="number"
                        className="w-20 p-2 border rounded-md"
                    />
                    <input type="range" className="w-full" />
                </div>
                <div className="flex justify-between text-sm text-gray-600 mt-2">
                    <span>$0</span>
                    <span>$1000</span>
                </div>
            </div>

            {/* Category Filter  */}
            <div className="bg-white p-4 rounded-lg shadow">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Category
                </label>
                <select className="w-full p-2 border rounded-md">
                    <option value="">All Categories</option>
                    <option value="1">Book</option>
                    <option value="2">Fashion</option>
                </select>
            </div>

            {/* Search  */}
            <div className="bg-white p-4 rounded-lg shadow">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Search
                </label>
                <input
                    type="text"
                    placeholder="Search books ..."
                    className="w-full p-2 border rounded-md"
                />
            </div>

            {/* Sorting  */}
            <div className="bg-white p-4 rounded-lg shadow">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Sort by Price
                </label>
                <select className="w-full p-2 border rounded-md">
                    <option value="">Default</option>
                    <option value="asc">Price: Low to High</option>
                    <option value="desc">Price: High to Low</option>
                </select>
            </div>
        </div>
    );
};

export default FilterSection;
