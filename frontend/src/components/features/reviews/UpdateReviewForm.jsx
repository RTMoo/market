import { useState } from "react";
import { toast } from "react-toastify";
import { updateReview } from "../../../api/review";

const UpdateReviewForm = ({ review, setBuyerReview, onClose }) => {
    const [loading, setLoading] = useState(false);
    const [formData, setFormData] = useState({
        comment: review.comment,
        rating: review.rating,
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
            const response = await updateReview(review.id, formData);
            if (response.status === 200) {
                setBuyerReview(response.data);
                toast.success("Отзыв обновлен");
                onClose();
            }
        } catch (error) {
            toast.error(error.detail || "Ошибка обновления отзыва");
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="mb-6 p-4 border rounded-lg bg-gray-100">
            <h2 className="text-lg font-semibold mb-2">Редактировать отзыв</h2>

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

            <div className="flex gap-2">
                <button
                    type="submit"
                    className="flex-1 bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 disabled:bg-gray-400"
                    disabled={loading}
                >
                    {loading ? "Обновление..." : "Обновить"}
                </button>
                <button
                    type="button"
                    className="flex-1 bg-gray-300 text-black py-2 rounded-md hover:bg-gray-400"
                    onClick={onClose}
                >
                    Отмена
                </button>
            </div>
        </form>
    );
};

export default UpdateReviewForm;