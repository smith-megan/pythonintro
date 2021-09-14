current_movies={'inception':'8:00am',
'tenet':'9pm',
}

print('we are showing these movies:')
for key in current_movies:
  print(key)
movie=input('what movie showtimes would you like?\n')
showtime=current_movies.get(movie)
if showtime==None:
  print('requested', movie, 'showtime is not playing')
else:
  print(movie, 'is playing at', showtime)