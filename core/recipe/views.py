from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

def get_recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        # print(recipe_name, recipe_description,recipe_image)
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
        )

        return redirect('/recipe/')
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
    return render(request,'recipe.html',context={'recipes':recipes})

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect("/recipe/")

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect("/recipe/")
    return render(request,'update_recipes.html',context={'recipe':queryset})