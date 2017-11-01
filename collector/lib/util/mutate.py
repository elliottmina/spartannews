def mutate(mutators, mutatee):
	for mutator in mutators:
		mutatee = mutator.mutate(mutatee)
	return mutatee
