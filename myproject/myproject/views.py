# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')

def foodrecipes(request):
    # return HttpResponse("My Food Recipes page.")
    return render(request, 'foodrecipes.html')

def vegetarian(request):
    return render(request, 'vegetarian.html')

def desserts(request):
    return render(request, 'desserts.html')

def holidays(request):
    return render(request, 'holidays.html')

def breakfast(request):
    return render(request, 'breakfast.html')

def lunch(request):
    return render(request, 'lunch.html')

def dinner(request):
    return render(request, 'dinner.html')

def dailyrecipes(request):
    return render(request, 'dailyrecipes.html')


def spaghetti(request):
    ingredients = [
        "400g spaghetti",
        "2 tbsp olive oil",
        "1 onion, finely chopped",
        "2 garlic cloves, minced",
        "400g canned tomatoes",
        "2 tsp dried oregano",
        "Salt and pepper to taste",
        "Fresh basil for garnish",
        "Grated Parmesan cheese for serving"
    ]

    instructions = [
        "Cook the spaghetti according to package instructions in a large pot of salted boiling water.",
        "In a separate pan, heat olive oil over medium heat. Add the chopped onion and cook until soft.",
        "Add the minced garlic and cook for another minute until fragrant.",
        "Stir in the canned tomatoes and oregano. Season with salt and pepper. Let it simmer for about 10-15 minutes.",
        "Once the spaghetti is cooked, drain it and add it to the sauce. Toss to combine.",
        "Serve hot, garnished with fresh basil and grated Parmesan cheese."
    ]

    return render(request, 'spaghetti.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })



def chickentikka(request):
    ingredients = [
        "500g chicken breast, cut into chunks",
        "1 cup plain yogurt",
        "2 tbsp lemon juice",
        "2 tsp ground cumin",
        "2 tsp paprika",
        "1 tsp ground turmeric",
        "1 tsp garam masala",
        "2 tbsp vegetable oil",
        "1 large onion, finely chopped",
        "3 garlic cloves, minced",
        "1 tbsp grated ginger",
        "1 can (400g) diced tomatoes",
        "1 cup heavy cream",
        "Salt and pepper to taste",
        "Fresh cilantro for garnish"
    ]

    instructions = [
        "In a bowl, mix yogurt, lemon juice, cumin, paprika, turmeric, and garam masala. Add chicken and marinate for at least 1 hour.",
        "Heat oil in a large pan over medium heat. Add onions and cook until golden brown.",
        "Add garlic and ginger, and cook for 1-2 minutes until fragrant.",
        "Stir in diced tomatoes and cook for 5 minutes.",
        "Add marinated chicken and cook until the chicken is fully cooked.",
        "Stir in heavy cream and simmer for 10 minutes. Season with salt and pepper.",
        "Garnish with fresh cilantro and serve with rice or naan bread."
    ]

    return render(request, 'chickentikka.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def vegetablestirfry(request):
    ingredients = [
        "2 tablespoons vegetable oil",
        "1 onion, sliced",
        "2 carrots, julienned",
        "1 bell pepper, sliced (red or yellow)",
        "1 cup broccoli florets",
        "1 cup snap peas",
        "2 cloves garlic, minced",
        "1 teaspoon fresh ginger, minced",
        "3 tablespoons soy sauce",
        "1 tablespoon sesame oil",
        "Salt and pepper to taste",
        "Fresh cilantro for garnish (optional)",
        "Cooked rice or noodles for serving"
    ]

    instructions = [
        "Heat the vegetable oil in a large wok or skillet over medium-high heat.",
        "Add the sliced onion and carrots, and stir-fry for about 2 minutes until they start to soften.",
        "Add the bell pepper, broccoli, and snap peas, and continue to stir-fry for another 3-5 minutes until the vegetables are tender-crisp.",
        "Stir in the minced garlic and ginger, cooking for an additional 30 seconds until fragrant.",
        "In a small bowl, mix the soy sauce and sesame oil until well combined.",
        "Pour the sauce over the stir-fried vegetables and toss to coat evenly. Cook for another minute until heated through.",
        "Season with salt and pepper to taste, and serve hot over rice or noodles, garnished with fresh cilantro if desired."
    ]

    return render(request, 'vegetablestirfry.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def chocolatevelvetcake(request):
    ingredients = [
        "2 cups all-purpose flour",
        "1 ¾ cups granulated sugar",
        "¾ cup unsweetened cocoa powder",
        "1 ½ teaspoons baking powder",
        "1 ½ teaspoons baking soda",
        "1 teaspoon salt",
        "2 large eggs",
        "1 cup whole milk",
        "½ cup vegetable oil",
        "2 teaspoons vanilla extract",
        "1 cup boiling water"
    ]

    instructions = [
        "Preheat your oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.",
        "In a large mixing bowl, combine the flour, sugar, cocoa powder, baking powder, baking soda, and salt. Whisk together until well combined.",
        "Add the eggs, milk, vegetable oil, and vanilla extract to the dry ingredients. Beat on medium speed for about 2 minutes until smooth.",
        "Carefully stir in the boiling water. The batter will be thin, but this is normal.",
        "Pour the batter evenly into the prepared cake pans. Bake for 30-35 minutes, or until a toothpick inserted in the center comes out clean. Allow the cakes to cool in the pans for 10 minutes, then remove from pans and cool completely on wire racks.",
        "In a mixing bowl, beat the softened butter and cream cheese together until creamy. Gradually add the powdered sugar and cocoa powder, mixing until smooth. Add vanilla extract and enough milk to achieve your desired frosting consistency.",
        "Once the cakes are completely cool, place one layer on a serving plate. Spread a layer of frosting on top, then place the second layer on top. Frost the top and sides of the cake with the remaining frosting.",
        "Slice and serve your delicious Chocolate Velvet Cake. Enjoy with fresh berries or chocolate shavings if desired!"
    ]

    return render(request, 'chocolatevelvetcake.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def caesarsalad(request):
    ingredients = [
        "1 large head of romaine lettuce, chopped",
        "1 cup homemade croutons (or store-bought)",
        "½ cup grated Parmesan cheese",
        "Freshly ground black pepper to taste",
        "1 clove garlic, minced",
        "2 anchovy fillets (optional)",
        "1 egg yolk (or 1 tablespoon mayonnaise for a no-raw-egg version)",
        "2 tablespoons lemon juice",
        "1 teaspoon Dijon mustard",
        "½ cup olive oil",
        "Salt and pepper to taste"
    ]

    instructions = [
        "In a bowl, whisk together the minced garlic, anchovy fillets (if using), egg yolk, lemon juice, and Dijon mustard until well combined.",
        "Slowly drizzle in the olive oil while whisking continuously until the dressing is emulsified. Season with salt and pepper to taste.",
        "In a large salad bowl, combine the chopped romaine lettuce and croutons.",
        "Drizzle the Caesar dressing over the salad and toss gently to coat the lettuce evenly.",
        "Sprinkle the grated Parmesan cheese over the top of the salad. Add freshly ground black pepper to taste.",
        "Serve immediately as a side dish or a light main course."
    ]

    return render(request, 'caesarsalad.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def birriatacos(request):
    ingredients = [
        "2 lbs beef chuck roast, cut into chunks",
        "4 dried guajillo chiles, stems and seeds removed",
        "2 dried ancho chiles, stems and seeds removed",
        "1 onion, quartered",
        "4 cloves garlic",
        "2 teaspoons ground cumin",
        "1 teaspoon dried oregano",
        "1 teaspoon salt",
        "1 teaspoon black pepper",
        "4 cups beef broth",
        "Corn tortillas",
        "1 cup shredded mozzarella cheese",
        "Chopped onions and cilantro for garnish",
        "Lime wedges for serving"
    ]

    instructions = [
        "In a pot, combine the beef, guajillo chiles, ancho chiles, onion, garlic, cumin, oregano, salt, and pepper.",
        "Add the beef broth and bring to a boil. Reduce heat and simmer for about 2-3 hours until the beef is tender.",
        "Remove the beef and shred it using two forks. Strain the broth and reserve it for dipping.",
        "Heat a skillet over medium heat. Dip a corn tortilla in the reserved broth, then place it on the skillet.",
        "Add a couple of tablespoons of shredded beef and a sprinkle of mozzarella cheese on one half of the tortilla.",
        "Fold the tortilla in half and cook until crispy and golden brown on both sides.",
        "Repeat with remaining tortillas and filling.",
        "Serve the tacos with chopped onions, cilantro, and lime wedges, along with a small bowl of the reserved broth for dipping."
    ]

    return render(request, 'birriatacos.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def pancakes(request):
    ingredients = [
        "1 cup all-purpose flour",
        "2 tablespoons granulated sugar",
        "2 teaspoons baking powder",
        "½ teaspoon baking soda",
        "¼ teaspoon salt",
        "1 cup buttermilk (or regular milk with 1 tablespoon vinegar added)",
        "1 large egg",
        "2 tablespoons unsalted butter, melted",
        "1 teaspoon vanilla extract (optional)"
    ]

    instructions = [
        "In a large bowl, whisk together the flour, sugar, baking powder, baking soda, and salt until well combined.",
        "In another bowl, mix the buttermilk, egg, melted butter, and vanilla extract (if using) until smooth.",
        "Pour the wet ingredients into the dry ingredients. Stir gently until just combined. Be careful not to overmix; a few lumps are okay.",
        "Heat a non-stick skillet or griddle over medium heat. Lightly grease with butter or oil.",
        "Pour about ¼ cup of batter onto the skillet for each pancake. Cook until bubbles form on the surface and the edges look set, about 2-3 minutes. Flip and cook for another 1-2 minutes until golden brown.",
        "Serve warm with your favorite toppings, such as maple syrup, fresh fruit, or whipped cream."
    ]

    return render(request, 'pancakes.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
    
    
def shrimpfriedrice(request):
    ingredients = [
        "2 cups cooked rice (preferably day-old)",
        "1 lb shrimp, peeled and deveined",
        "2 tablespoons vegetable oil",
        "1 cup peas and carrots (frozen or fresh)",
        "3 green onions, chopped",
        "2 eggs, beaten",
        "3 tablespoons soy sauce",
        "1 tablespoon sesame oil",
        "Salt and pepper to taste"
    ]

    instructions = [
        "Heat 1 tablespoon of vegetable oil in a large skillet or wok over medium-high heat.",
        "Add the shrimp and cook until pink and opaque, about 2-3 minutes. Remove the shrimp from the skillet and set aside.",
        "In the same skillet, add the remaining tablespoon of oil. Add the peas and carrots, and cook for 2-3 minutes until tender.",
        "Push the vegetables to one side of the skillet and pour the beaten eggs into the other side. Scramble the eggs until fully cooked.",
        "Add the cooked rice to the skillet, breaking up any clumps. Stir everything together.",
        "Return the cooked shrimp to the skillet. Add soy sauce, sesame oil, salt, and pepper. Stir-fry for another 2-3 minutes until everything is heated through.",
        "Garnish with chopped green onions and serve hot."
    ]

    return render(request, 'shrimpfriedrice.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def mushroomrisotto(request):
    ingredients = [
        "1 cup Arborio rice",
        "4 cups vegetable or chicken broth",
        "1 cup white wine",
        "1 medium onion, finely chopped",
        "2 cloves garlic, minced",
        "8 oz mushrooms, sliced (such as cremini or button)",
        "2 tablespoons olive oil",
        "2 tablespoons unsalted butter",
        "½ cup grated Parmesan cheese",
        "Salt and pepper to taste",
        "Fresh parsley for garnish (optional)"
    ]

    instructions = [
        "In a saucepan, heat the broth over low heat and keep it warm.",
        "In a large skillet, heat the olive oil and 1 tablespoon of butter over medium heat. Add the chopped onion and cook until translucent, about 5 minutes.",
        "Add the garlic and sliced mushrooms to the skillet. Sauté until the mushrooms are tender and browned, about 5-7 minutes.",
        "Stir in the Arborio rice and cook for 1-2 minutes until the rice is lightly toasted.",
        "Pour in the white wine and cook, stirring constantly, until the wine is mostly absorbed.",
        "Begin adding the warm broth, one ladle at a time, stirring frequently. Allow the rice to absorb most of the liquid before adding more broth. Continue this process until the rice is creamy and al dente, about 18-20 minutes.",
        "Remove from heat and stir in the remaining tablespoon of butter and the grated Parmesan cheese. Season with salt and pepper to taste.",
        "Garnish with fresh parsley if desired and serve hot."
    ]

    return render(request, 'mushroomrisotto.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
    
def cheesecake(request):
    ingredients = [
        "1 ½ cups graham cracker crumbs",
        "½ cup unsalted butter, melted",
        "1 cup granulated sugar",
        "4 (8 oz) packages cream cheese, softened",
        "1 teaspoon vanilla extract",
        "4 large eggs",
        "1 cup sour cream",
        "¼ cup all-purpose flour",
        "Zest of 1 lemon (optional)",
        "Fresh fruit or fruit sauce for topping (optional)"
    ]

    instructions = [
        "Preheat your oven to 325°F (160°C).",
        "In a medium bowl, combine the graham cracker crumbs and melted butter. Press the mixture into the bottom of a 9-inch springform pan to form the crust.",
        "In a large mixing bowl, beat the softened cream cheese until smooth. Gradually add the sugar and mix until well combined.",
        "Add the vanilla extract, eggs (one at a time), sour cream, flour, and lemon zest (if using). Mix until smooth and creamy.",
        "Pour the cheesecake batter over the crust in the springform pan.",
        "Bake in the preheated oven for 55-60 minutes, or until the center is set and slightly jiggly.",
        "Turn off the oven and leave the cheesecake inside for 1 hour to cool gradually.",
        "Remove from the oven and let it cool completely at room temperature. Refrigerate for at least 4 hours or overnight before serving.",
        "Top with fresh fruit or fruit sauce if desired, slice, and enjoy!"
    ]

    return render(request, 'cheesecake.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    

def tiramisu(request):
    ingredients = [
        "6 egg yolks",
        "¾ cup granulated sugar",
        "2/3 cup milk",
        "1 ¼ cups heavy cream",
        "8 oz mascarpone cheese, softened",
        "1 cup strong brewed coffee, cooled",
        "3 tablespoons coffee liqueur (optional)",
        "24 ladyfinger cookies",
        "Cocoa powder for dusting",
        "Dark chocolate shavings for garnish (optional)"
    ]

    instructions = [
        "In a medium saucepan, whisk together the egg yolks and sugar until well combined.",
        "Add the milk to the saucepan and cook over medium heat, stirring constantly until the mixture thickens and coats the back of a spoon. Remove from heat and let it cool slightly.",
        "In a large bowl, whip the heavy cream until stiff peaks form. Gently fold in the mascarpone cheese until smooth.",
        "Combine the cooled milk mixture with the mascarpone mixture, folding gently until fully incorporated.",
        "In a shallow dish, combine the brewed coffee and coffee liqueur (if using). Quickly dip each ladyfinger into the coffee mixture, making sure not to soak them.",
        "Layer half of the dipped ladyfingers in the bottom of a 9x9 inch dish. Spread half of the mascarpone mixture over the ladyfingers.",
        "Repeat with another layer of dipped ladyfingers and the remaining mascarpone mixture.",
        "Cover and refrigerate for at least 4 hours, preferably overnight.",
        "Before serving, dust the top with cocoa powder and garnish with dark chocolate shavings if desired."
    ]

    return render(request, 'tiramisu.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
    

def lentilsoup(request):
    ingredients = [
        "1 cup dried lentils (green or brown)",
        "1 onion, chopped",
        "2 carrots, diced",
        "2 celery stalks, diced",
        "4 cups vegetable broth",
        "1 teaspoon ground cumin",
        "Salt and pepper to taste",
        "2 tablespoons olive oil",
        "1 bay leaf",
        "Fresh parsley for garnish (optional)"
    ]

    instructions = [
        "1. Rinse the lentils under cold water and set aside.",
        "2. In a large pot, heat olive oil over medium heat. Add chopped onion, carrots, and celery; sauté until softened, about 5-7 minutes.",
        "3. Stir in the rinsed lentils, vegetable broth, cumin, bay leaf, salt, and pepper.",
        "4. Bring the mixture to a boil, then reduce the heat to low and cover. Let it simmer for about 30-40 minutes, or until the lentils are tender.",
        "5. Remove the bay leaf and adjust seasoning if necessary.",
        "6. Serve hot, garnished with fresh parsley if desired."
    ]

    return render(request, 'lentil_soup.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    

def glazedham(request):
    ingredients = [
        "1 fully cooked ham (about 8-10 lbs)",
        "1 cup brown sugar",
        "1/2 cup honey",
        "1/4 cup Dijon mustard",
        "1/4 cup apple cider vinegar",
        "1 teaspoon ground cloves",
        "1 teaspoon ground cinnamon",
        "1/2 teaspoon black pepper"
    ]
    instructions = [
        "1. Preheat the oven to 325°F (165°C).",
        "2. In a bowl, mix together brown sugar, honey, Dijon mustard, apple cider vinegar, cloves, cinnamon, and black pepper to create the glaze.",
        "3. Place the ham in a roasting pan and score the surface in a diamond pattern.",
        "4. Brush half of the glaze over the ham.",
        "5. Cover with foil and bake for 1 hour.",
        "6. Remove the foil and brush with remaining glaze. Bake uncovered for an additional 30-45 minutes, basting every 15 minutes.",
        "7. Let it rest for 15 minutes before slicing."
    ]
    return render(request, 'glazedham.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
    
def pumpkinpie(request):
    ingredients = [
        "1 (15 oz) can pumpkin puree",
        "1 cup heavy cream",
        "3/4 cup brown sugar",
        "1/2 cup granulated sugar",
        "3 large eggs",
        "1 teaspoon vanilla extract",
        "1 teaspoon ground cinnamon",
        "1/2 teaspoon ground nutmeg",
        "1/2 teaspoon ground ginger",
        "1/4 teaspoon ground cloves",
        "1/2 teaspoon salt",
        "1 (9-inch) unbaked pie crust"
    ]

    instructions = [
        "1. Preheat the oven to 425°F (220°C).",
        "2. In a large bowl, whisk together the pumpkin puree, heavy cream, brown sugar, granulated sugar, eggs, and vanilla extract until smooth.",
        "3. Add the cinnamon, nutmeg, ginger, cloves, and salt to the mixture and whisk until well combined.",
        "4. Pour the pumpkin filling into the unbaked pie crust.",
        "5. Bake in the preheated oven for 15 minutes.",
        "6. Reduce the temperature to 350°F (175°C) and continue baking for an additional 35-40 minutes, or until the filling is set and a knife inserted in the center comes out clean.",
        "7. Remove from the oven and let the pie cool on a wire rack.",
        "8. Serve chilled or at room temperature, optionally topped with whipped cream."
    ]

    return render(request, 'pumpkinpie.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })
    
def roastturkey(request):
    ingredients = [
        "1 whole turkey (12-14 pounds, thawed)",
        "1/2 cup unsalted butter, softened",
        "2 tablespoons olive oil",
        "2 teaspoons salt",
        "1 teaspoon black pepper",
        "1 tablespoon fresh rosemary, chopped",
        "1 tablespoon fresh thyme, chopped", 
        "1 tablespoon fresh sage, chopped",
        "1 onion, quartered",
        "1 lemon, quartered",
        "4 cups low-sodium chicken broth",
        "Fresh herbs for garnish (optional)"
    ]

    instructions = [
        "1. Preheat the oven to 325°F (165°C).",
        "2. Remove turkey from packaging and remove giblets from cavity. Pat turkey dry with paper towels.",
        "3. In a bowl, mix softened butter, olive oil, salt, pepper, and chopped herbs.",
        "4. Carefully loosen skin over turkey breast and spread herb butter mixture underneath and on top of skin.",
        "5. Stuff turkey cavity with quartered onion and lemon.",
        "6. Place turkey breast-side up on a rack in a roasting pan. Pour chicken broth into the bottom of the pan.",
        "7. Roast turkey for approximately 13-15 minutes per pound, basting every 30 minutes.",
        "8. Check internal temperature. Turkey is done when thickest part of thigh reaches 165°F (74°C).",
        "9. Remove from oven and let rest for 20-30 minutes before carving.",
        "10. Carve and serve with your favorite side dishes."
    ]

    return render(request, 'roastturkey.html', {
        'ingredients': ingredients,
        'instructions': instructions
    })