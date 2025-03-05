const Paginator = ({ next, previous, onPageChange }) => {
    return (
            <div className="w-40 flex justify-between">
                <button onClick={() => onPageChange(previous)} disabled={!previous}>
                    ← Назад
                </button>
                <button onClick={() => onPageChange(next)} disabled={!next}>
                    Вперед →
                </button>
            </div>
    );
};

export default Paginator;
