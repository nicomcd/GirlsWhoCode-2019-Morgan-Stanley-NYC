import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

string2 = ('''Two households, both alike in dignity In fair Verona, where we lay our scene, From ancient grudge break to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-crossed lovers take their life;
Whose misadventured piteous overthrows
Doth with their death bury their parents’ strife.
The fearful passage of their death-marked love
And the continuance of their parents’ rage,
Which, but their children’s end, naught could remove,
Is now the two hours’ traffic of our stage;
The which, if you with patient ears attend,
What here shall miss, our toil shall strive to mend. SAMPSON
GREGORY
SAMPSON
GREGORY
SAMPSON
GREGORY
SAMPSON
GREGORY
SAMPSON
GREGORY
SAMPSON
GREGORY
SAMPSON
Enter Sampson and Gregory, with swords and bucklers,
of the house of Capulet.
Gregory, on my word we’ll not carry coals.
No, for then we should be colliers.
I mean, an we be in choler, we’ll draw.
Ay, while you live, draw your neck out of
collar.
I strike quickly, being moved.
But thou art not quickly moved to strike.
A dog of the house of Montague moves me.
To move is to stir, and to be valiant is to
stand. Therefore if thou art moved thou runn’st
away.
A dog of that house shall move me to stand. I
will take the wall of any man or maid of Montague’s.
That shows thee a weak slave, for the weakest
goes to the wall.
’Tis true, and therefore women, being the
weaker vessels, are ever thrust to the wall. Therefore
I will push Montague’s men from the wall and
thrust his maids to the wall.
The quarrel is between our masters and us
their men.
’Tis all one. I will show myself a tyrant.
When I have fought with the men, I will be civil
with the maids; I will cut off their heads. ''')

wordcloud = WordCloud().generate(string2)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig('nicoleandjulietandromeo.png')
