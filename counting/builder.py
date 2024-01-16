import string
import random

def build_meaningful():
    meaningful = '''
    According to his plan, Hamlet begins to act strangely. He rejects Ophelia, while Claudius and Polonius, the royal attendant, spy on him. They had hoped to find the reason for Hamlet's sudden change in behaviour but could not. Claudius summons Guildenstern and Rosencrantz, old friends of Hamlet to find out what's got into him. Their arrival coincides with a group of travelling actors that Hamlet happens to know well. Hamlet writes a play which includes scenes that mimic the murder of Hamlet's father. During rehearsal, Hamlet and the actors plot to present Hamlet's play before the King and Queen. 
    At the performance, Hamlet watches Claudius closely to see how he reacts. The play provokes Claudius, and he interrupts the action by storming out. He immediately resolves to send Hamlet away. Hamlet is summoned by his distressed mother, Gertrude, and on the way, he happens upon Claudius kneeling and attempting to pray. Hamlet reasons that to kill the King now would only send his soul to heaven rather than hell. Hamlet decides to spare his life for the time being.
    Polonius hides in Gertrude's room to protect her from her unpredicatable son. When Hamlet arrives to scold his mother, he hears Polonius moving behind the arras (a kind of tapestry). He stabs the tapestry and, in so doing, kills Polonius. The ghost of Hamlet's father reappears and warns his son not to delay revenge or upset his mother.
    Hamlet is sent to England, supposedly as an ambassador, just as King Fortinbras of Norway crosses Denmark with an army to attack Poland. During his journey, Hamlet discovers Claudius has a plan to have him killed once he arrives. He returns to Denmark alone, sending his companions Rosencrantz and Guildenstern to their deaths in his place. 

    Rejected by Hamlet, Ophelia is now desolate at the loss of her father. She goes mad and drowns. 
    On the way back to Denmark, Hamlet meets Horatio in the graveyard (along with a gravedigger), where they talk of the chances of life and death. Ophelia's funeral procession arrives at the very same graveyard (what luck!). Hamlet confronts Laertes, Ophelia's brother, who has taken his father's place at the court. 

    A duel is arranged between Hamlet and Laertes. During the match, Claudius conspires with Laertes to kill Hamlet. They plan that Hamlet will die either on a poisoned rapier or with poisoned wine. The plans go awry when Gertrude unwittingly drinks from the poisoned cup and dies. Then both Laertes and Hamlet are wounded by the poisoned blade, and Laertes dies. 

    Hamlet, in his death throes, kills Claudius. Hamlet dies, leaving only his friend Horatio to explain the truth to the new king, Fortinbras, as he returns in victory from the Polish wars.
    The ghost of the King of Denmark tells his son Hamlet to avenge his murder by killing the new king, Hamlet's uncle. Hamlet feigns madness, contemplates life and death, and seeks revenge. His uncle, fearing for his life, also devises plots to kill Hamlet. The play ends with a duel, during which the King, Queen, Hamlet's opponent and Hamlet himself are all killed. 
    Late at night, guards on the battlements of Denmark's Elsinore castle are met by Horatio, Prince Hamlet's friend from school. The guards describe a ghost they have seen that resembles Hamlet's father, the recently-deceased king. At that moment, the Ghost reappears, and the guards and Horatio decide to tell Hamlet.

    Claudius, Hamlet's uncle, married Hamlet's recently-widowed mother, becoming the new King of Denmark. Hamlet continues to mourn for his father's death and laments his mother's lack of loyalty. When Hamlet hears of the Ghost from Horatio, he wants to see it for himself. 

    Elsewhere, the royal attendant Polonius says farewell to his son Laertes, who is departing for France. Laertes warns his sister, Ophelia, away from Hamlet and thinking too much of his attentions towards her. 
    aberration  abjure  abnegation  abrogate  preponderance  presage  probity  tirade  wily 
    winsome  vociferous  vituperate  vilify variation in circumstances or fortune  vicissitude
    There are surviving manuscripts written in both Latin and local languages. Irish missionaries are thought to have been responsible for the script used in early Anglo-Saxon documents, including the Insular semi-Uncial (an important Latin text) and the Insular (both Latin and vernacular). In the 10th century, Caroline miniatures were adopted for Latin, but insular miniatures continued to be used for Old English texts. After that, it became more and more influenced by Caroline Minicules, while maintaining the island nation's peculiar writing style. Early English manuscripts often contain later annotations in the margins of the text. It is unusual to find manuscripts that are completely unannotated. These include corrections, alterations, extensions to the text, commentary on the text, and even unrelated text. Most of these annotations appear to date from the 13th century onwards.
    Although all extant Old English poetry is written and literate, many scholars argue that Old English poetry was an oral craft played on a scoop accompanied by a harp. Millman Parry and Albert Lord's hypothesis about the Homer problem went like this: It was applied (by Parry and Lord, but also by Francis Magoon) to poetry written in Old English. That is, the theory proposes that at least some particular characteristics of poetry may be explained by assuming an oral-formal construction. Old English epics may bear some resemblance to ancient Greek epics such as the Iliad and the Odyssey, but the question of whether and how Anglo-Saxon poetry was passed down through oral tradition is It remains a matter of debate and a question for specific poems. Parry and Lord had already demonstrated prosody density in Ancient Greek, and observed the same characteristics in Old English alliteration lines. In addition to verbal formulas, many themes have been shown to appear in various works of Anglo-Saxon literature. This theory suggests why. Poetry consisted of formulas and themes from the stock common to the poetic profession, as well as literary passages composed by individual artists in a more contemporary sense. Larry Benson introduced the concept of "written formulaic" to describe the situation of some Anglo-Saxon poetry. The poem, although clearly written, contains evidence of oral influence, including a heavy reliance on formulas and subject matter. Frequent orally stylized themes in Old English poetry include "fighting beasts" and "death cliffs". The former, for example, is characterized by references to crows, eagles, and wolves preceding particularly violent depictions of combat. Among the most thoroughly documented themes are "beach heroes". D. K. Crowne first proposed this theme and defined it by four characteristics: beach hero. Accompany the "retainer". flashing lights. Completion or commencement of a journey. One example that Crown cites in the article is the ending of Beowulf's battle with the monster during a swimming match with Breka. Crown elicited examples of the theme's occurrence in 12 Old English texts, including one occurrence in Beowulf. It was found in other works of Germanic origin, in Middle English poetry, and even in Icelandic prose tales. John Richardson believes that this schema is so general that it can be applied to virtually any character at some point in the story, calling this the "threshold" function in Joseph Campbell's Heroes' Journey Monomyth. I thought it was an example. J.A. Dehn, in a paper (characterized by Foley as "a controversy without rigor"), argues that the appearance of the subject in ancient Greek poetry, a tradition with no known Germanic connection, was "a human arguing that it invalidates the notion of "autonomous subjects in the baggage of Oral poet. Foley's reply was that Dane misunderstood the nature of oral tradition, and that in fact the appearance of the subject in other cultures indicated that it was a traditional form.
    '''
    words = meaningful.replace(",","").replace("(","").replace(")","").replace(".","").replace("?","").replace("!","")
    with open('dataset/meaningful.txt', 'w') as f:
        for line in set(words.split()):
            f.write("%s\n" % line)


def word_maker():
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    all_words = []
    for i in string.ascii_lowercase:
        for j in range(50):
            num = random.randint(2, 15)
            word = random.choices(alphabet, k=num)
            if num <= 4:
                f = random.randint(1, 6)
                word += [i] * f + [i] * f
            
            word = "".join(random.sample(word, len(word)))
            all_words.append(word)
    return all_words


def num_maker():
    nums = []
    counts = [30, 100, 150, 150, 200, 300, 300]
    for i in range(1, 8):
        for k in range(counts[i - 1]):
            nums.append(random.randint(10**i, 10 ** (i + 1)))
    return nums

def num_word_maker():
    nums = []
    letters = string.ascii_letters
    numbers = string.digits
    for i in range(550):
        num_letters = random.randint(2, 10)
        num_digits = random.randint(0, 9)
        num = random.choices(letters, k = num_letters) + random.choices(numbers, k = num_digits)
        num = random.sample(num, k = len(num))
        
        nums.append("".join(num))
    return nums

with open('word_num1000.txt', 'w') as f:
    for line in word_maker():
        f.write("%s\n" % line)
