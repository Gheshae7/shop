from django.shortcuts import render
from comment_module.models import Comment
from django.http import JsonResponse, HttpRequest, HttpResponse
from product_module.models import Product
from django.template.loader import render_to_string
# Create your views here.


def comments_product(request: HttpRequest, product_id: int) -> HttpResponse:
    comments: Comment = (
        Comment.objects.filter(is_active=True, product_id=product_id)
        .select_related("user")
        .order_by("-created_at")
    )
    context = {"comments": comments}

    return render(
        request, "comment_module/component_partial/single_comment.html", context
    )


def add_commnet(request: HttpRequest) -> JsonResponse | HttpResponse:
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                product_id = request.POST.get("product_id")
                current_product: Product = Product.objects.get(
                    is_active=True, id=product_id
                )
                rating = request.POST.get("rating")
                if rating.isalpha() or int(rating) < 0 or int(rating) > 5:
                    return JsonResponse(
                        {
                            "icon": "warning",
                            "message": "امتیاز محصول باید بین 1 تا 5 باشد",
                        }
                    )
                else:
                    message = request.POST.get("message")
                    Comment.objects.create(
                        is_active=True,
                        user_id=request.user.id,
                        product_id=current_product.id,
                        message=message,
                        rating=int(rating),
                    )

                    comments = (
                        Comment.objects.filter(is_active=True, product_id=product_id)
                        .select_related("user")
                        .order_by("-created_at")
                    )

                    comments_product = render_to_string(
                        "comment_module/component_partial/single_comment.html",
                        {"comments": comments},
                        request=request,
                    )

                    # return comments_product(request=request, product_id=product_id)
                    return JsonResponse(
                        {
                            "comments_product": comments_product,
                            "count_comment_product": Comment.objects.filter(
                                product_id=product_id
                            ).count(),
                        }
                    )
            except Product.DoesNotExist:
                return JsonResponse(
                    {"icon": "error", "message": "محصول مورد نظر پیدا نشد"}
                )
        else:
            return JsonResponse(
                {
                    "icon": "info",
                    "message": "برای کامنت گذاشتن ابتدا باید وارد حساب کاربر خود شوید",
                }
            )
