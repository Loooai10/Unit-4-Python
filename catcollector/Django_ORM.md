1. Retrieve all cats:
-Cat.objects.all()
  Retrieve first row of query
-Cat.object

2. Create a new Cat:
-catInstance = Cat(name=",.. .. .)

3. Save changes to an existing queryset
-catInstance.save()

4. Filter Cats from DB:
-Cat.object,filter(name=' .. ... .)
-Cat.objects.filter(nam_contains=' .. ...')
-Cat.objects.filte(age_lte= .. ... .. )




7. Retrieve all Feedings of a Cat (1:M, ForeignKey)
- c = Cat.object