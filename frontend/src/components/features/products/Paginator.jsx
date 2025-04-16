const Paginator = ({ next, previous, current, total, onPageChange }) => {
    const getPages = () => {
        const pages = [];
        for (let i = 1; i <= total; i++) {
            pages.push(i);
        }
        return pages;
    };

    return (
        <div className="flex items-center space-x-2">
            <button
                onClick={() => onPageChange(previous)}
                disabled={!previous}
                className="px-3 py-1 border rounded disabled:opacity-50"
            >
                ← Назад
            </button>

            {getPages().map((page) => (
                <button
                    key={page}
                    onClick={() => onPageChange(page)}
                    className={`px-3 py-1 border rounded ${
                        current === page ? 'bg-black text-white' : ''
                    }`}
                >
                    {page}
                </button>
            ))}

            <button
                onClick={() => onPageChange(next)}
                disabled={!next}
                className="px-3 py-1 border rounded disabled:opacity-50"
            >
                Вперед →
            </button>
        </div>
    );
};

export default Paginator;
