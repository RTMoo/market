import { useState, useEffect } from "react";
import { getProductReviews, deleteReview } from "../../../api/review";
import AddReviewForm from "./AddReviewForm";
import UpdateReviewForm from "./UpdateReviewForm";
import { VscEdit, VscDiffRemoved } from "react-icons/vsc";
import { toast } from "react-toastify";

const ProductReviews = ({ productId }) => {
    const [reviews, setReviews] = useState([]);
    const [buyerReview, setBuyerReview] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const fetchGetReviewList = async () => {
        try {
            const response = await getProductReviews(productId);
            if (response.status === 200) {
                setReviews(response.data.reviews);
                setBuyerReview(response.data.buyerReview);
            }
        } catch (error) {
            console.log(error);
        }
    };

    const hanldeDeleteReview = async () => {
        try {
            await deleteReview(buyerReview.id);
            setBuyerReview(null);
            toast.success("Отзыв удалён");
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        fetchGetReviewList();
    }, []);

    return (
        <div className="max-w-4xl mx-auto">
            <h1 className="text-2xl font-semibold mb-4 text-center">Отзывы</h1>

            {/* Форма для отзыва */}
            {!buyerReview && <AddReviewForm
                productId={productId}
                setBuyerReview={setBuyerReview}
                setReviews={setReviews}
            />}

            {/* Форма для редактирования отзыва */}

            {buyerReview && isEditing && (
                <UpdateReviewForm
                    review={buyerReview}
                    setBuyerReview={setBuyerReview}
                    onClose={() => setIsEditing(false)}
                />
            )}

            {/* Список отзывов */}
            <div className="flex flex-col gap-6">
                
                {buyerReview && (
                    <div key={buyerReview.id} className="border rounded-lg shadow-md p-4 pt-1 bg-gray-100 flex flex-col">
                        <div className="pb-3 flex items-center justify-between">
                            <h3 className="text-gray-600">Ваш комментарий</h3>
                            <div className="flex gap-4">
                                <VscEdit className="text-blue-500" size={20} onClick={() => setIsEditing(true)}/>
                                <VscDiffRemoved className="text-red-500" size={20} onClick={hanldeDeleteReview}/>
                            </div>
                            
                        </div>
                        <hr />
                        <div className="">
                        <div className="flex items-center justify-between">
                            <span className="font-semibold text-gray-700">{buyerReview.buyer}</span>
                            <span className="text-sm text-gray-500">
                                {new Date(buyerReview.created_at).toLocaleDateString()}
                            </span>
                        </div>
                        <div className="flex gap-1 mt-2 text-yellow-500">
                            {[...Array(buyerReview.rating)].map((_, i) => (
                                <span key={i}>★</span>
                            ))}
                        </div>
                        <p className="text-gray-800 mt-3">{buyerReview.comment}</p>
                        </div>
                    </div>
                )}

                {reviews.length > 0 ? (
                    reviews.map((review) => (
                        <div key={review.id} className="border rounded-lg shadow-md p-4 bg-gray-50">
                            <div className="flex items-center justify-between">
                                <span className="font-semibold text-gray-700">{review.buyer}</span>
                                <span className="text-sm text-gray-500">
                                    {new Date(review.created_at).toLocaleDateString()}
                                </span>
                            </div>
                            <div className="flex gap-1 mt-2 text-yellow-500">
                                {[...Array(review.rating)].map((_, i) => (
                                    <span key={i}>★</span>
                                ))}
                            </div>
                            <p className="text-gray-800 mt-3">{review.comment}</p>
                        </div>
                    ))
                ) : (
                    <p className="text-center text-gray-500">Отзывов пока нет.</p>
                )}
            </div>
        </div>
    );
};

export default ProductReviews;
