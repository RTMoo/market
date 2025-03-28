import { useState } from 'react';
import { toast } from "react-toastify";
import { createReview } from "../../../api/review";


const AddReviewForm = ({ productId, setBuyerReview, setReviews }) => {
    const [loading, setLoading] = useState(false);
    const [formData, setFormData] = useState({
        comment: "",
        rating: 0,
        product_id: productId
    });

    const handleInputChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleRatingChange = (value) => {
        setFormData({ ...formData, rating: value });
    };

    const handleSubmit = async (e) => {
        
        e.preventDefault();
        setLoading(true);
        try {
            const response = await createReview(formData);
            if (response.status === 201) {
                setBuyerReview(response.data);
                setReviews((prev) => prev.filter(r => r.id !== response.data.id));
                setFormData({ comment: "", rating: 0, product_id: productId });
            }
        } catch (error) {
            toast.error(error.detail);
        } finally {
            setLoading(false);
        }
    };
    return (
        <form onSubmit={handleSubmit} className="mb-6 p-4 border rounded-lg bg-gray-100">
            <h2 className="text-lg font-semibold mb-2">Оставить отзыв</h2>

            <div className="mb-3">
                <label className="block text-sm font-medium text-gray-700">Рейтинг</label>
                <div className="flex gap-1 mt-1">
                    {[1, 2, 3, 4, 5].map((star) => (
                        <button
                            type="button"
                            key={star}
                            className={`p-1 text-xl ${formData.rating >= star ? "text-yellow-500" : "text-gray-400"}`}
                            onClick={() => handleRatingChange(star)}
                        >
                            ★
                        </button>
                    ))}
                </div>
            </div>

            <div className="mb-3">
                <label className="block text-sm font-medium text-gray-700">Комментарий</label>
                <textarea
                    name="comment"
                    value={formData.comment}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2 border rounded-md"
                    rows="3"
                />
            </div>

            <button
                type="submit"
                className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 disabled:bg-gray-400"
                disabled={loading}
            >
                {loading ? "Отправка..." : "Оставить отзыв"}
            </button>
        </form>
    );
}

export default AddReviewForm;
