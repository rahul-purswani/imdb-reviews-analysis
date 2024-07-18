import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataframe1 = pd.read_csv('imdb.csv')
dataframe2 = pd.read_csv('commonUsers.csv')

#GETTING A LIST OF THE COMMON USERS WHO HAVE REVIEWED 5+ Movies in The Reviews
#print(dataframe2['USERNAME'][0])
listOfCommonUsers = []
for x in dataframe2['USERNAME']:
    listOfCommonUsers.append(x)

#Getting only the Reviews By Common Users
notInIndices = []
for y in range(dataframe1.shape[0]):
    if(dataframe1['Review_User'].loc[y] not in listOfCommonUsers):
        notInIndices.append(y)
dataframe1 = dataframe1.drop(dataframe1.index[notInIndices])
dataframe1 = dataframe1.rename_axis('index1').reset_index(drop=True)

#print(dataframe1.shape)
#print(len(listOfCommonUsers))


#GETTING A LIST OF ALL THE GENRES IN THE REVIEWS
a = dataframe1['Movie_Genres']
listOFGenres = []
for x in range(a.size):
    currentGenres = a[x]
    currentGenres = currentGenres.replace('\'', '')
    currentGenres = currentGenres.replace('[', '')
    currentGenres = currentGenres.replace(']', '')
    currentGenres = currentGenres.replace(' ', '')
    listOfCurrentGenres = currentGenres.split(",")
    for x in listOfCurrentGenres:
        if(x not in listOFGenres):
            #IF WE ARE HERE THE GENRE HASNT BEEN FOUND
            listOFGenres.append(x)
        
listOFGenres.sort()
#print(listOFGenres)
ratingCorrelations = []
allUsersAvgRtgs = []
allNumOfRatings = []
countofTotalRatings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for currUser in listOfCommonUsers:
    sumOfUsersRatings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    countofUserRatings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    avgUsersRatings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range(dataframe1.shape[0]):
        if(dataframe1['Review_User'].loc[x] == currUser):
            currMovieGenres = dataframe1['Movie_Genres'].loc[x]
            if("Action" in currMovieGenres):
                sumOfUsersRatings[0] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[0] += 1
            if("Adventure" in currMovieGenres):
                sumOfUsersRatings[1] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[1] += 1
            if("Animation" in currMovieGenres):
                sumOfUsersRatings[2] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[2] += 1
            if("Biography" in currMovieGenres):
                sumOfUsersRatings[3] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[3] += 1
            if("Comedy" in currMovieGenres):
                sumOfUsersRatings[4] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[4] += 1
            if("Crime" in currMovieGenres):
                sumOfUsersRatings[5] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[5] += 1
            if("Drama" in currMovieGenres):
                sumOfUsersRatings[6] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[6] += 1
            if("Family" in currMovieGenres):
                sumOfUsersRatings[7] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[7] += 1
            if("Fantasy" in currMovieGenres):
                sumOfUsersRatings[8] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[8] += 1
            if("Film-Noir" in currMovieGenres):
                sumOfUsersRatings[9] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[9] += 1
            if("History" in currMovieGenres):
                sumOfUsersRatings[10] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[10] += 1
            if("Horror" in currMovieGenres):
                sumOfUsersRatings[11] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[11] += 1
            if("Music" in currMovieGenres):
                sumOfUsersRatings[12] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[12] += 1
            if("Musical" in currMovieGenres):
                sumOfUsersRatings[13] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[13] += 1
            if("Mystery" in currMovieGenres):
                sumOfUsersRatings[14] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[14] += 1
            if("Romance" in currMovieGenres):
                sumOfUsersRatings[15] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[15] += 1
            if("Sci-Fi" in currMovieGenres):
                sumOfUsersRatings[16] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[16] += 1
            if("Sport" in currMovieGenres):
                sumOfUsersRatings[17] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[17] += 1
            if("Thriller" in currMovieGenres):
                sumOfUsersRatings[18] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[18] += 1
            if("War" in currMovieGenres):
                sumOfUsersRatings[19] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[19] += 1
            if("Western" in currMovieGenres):
                sumOfUsersRatings[20] += dataframe1['Review_Rating'].loc[x]
                countofUserRatings[20] += 1
    
    for x in range(21):
        countofTotalRatings[x] += countofUserRatings[x]
        if(countofUserRatings[x] != 0):
            avgUsersRatings[x] = sumOfUsersRatings[x] / countofUserRatings[x]
    allUsersAvgRtgs.append(avgUsersRatings)
    allNumOfRatings.append(countofUserRatings)            

contShow = True
while contShow:
    coords = pd.DataFrame(columns=['x','y'])
    for x in range(len(listOFGenres)):
        print(x, " : ", listOFGenres[x])
    xVal = int(input("Please Enter The Integer Value Associated With The First Genre You Would Like To Compare: "))
    yVal = int(input("Please Enter The Integer Value Associated With The Second Genre You Would Like To Compare: "))
    
    if(isinstance(xVal, int) and isinstance(yVal, int)):
        if(xVal >= 0 and xVal < 21 and yVal >= 0 and yVal < 21):
            #IF HERE THEY ENTERED 2 GENRE VALUES
            for x in range(len(listOfCommonUsers)):
               if(allUsersAvgRtgs[x][xVal] != 0 and allUsersAvgRtgs[x][yVal] != 0):
                    #print(allUsersAvgRtgs[x][xVal], allUsersAvgRtgs[x][yVal])
                    g = allNumOfRatings[yVal][0]
                    if(allNumOfRatings[xVal][0] > g):
                        g = allNumOfRatings[xVal][0]
                    for y in range(g):
                        c = [allUsersAvgRtgs[x][xVal], allUsersAvgRtgs[x][yVal]]
                        coords.loc[len(coords)] = c
            
            
            v = np.array(coords['x'])
            w = np.array(coords['y'])
            coords.columns = [listOFGenres[xVal], listOFGenres[yVal]]
            coords.plot(x=listOFGenres[xVal], y=listOFGenres[yVal], kind='scatter')
            if(v.size > 0 and w.size > 0):
                a, b = np.polyfit(v, w, 1)
                plt.plot(v, a*v + b)
            plt.show()
   
    contShow = int(input("Would You Like To See Another Plot (0 or 1): "))
    if(isinstance(contShow, int)):
        if(contShow == 1):
            contShow = True
        else:
            contShow = False
    else:
        contShow = False