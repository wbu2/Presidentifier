from cnn_predict import orchestrate

#python dictionary format
example_usage = {
    'url1': #article from the onion
        'Staging the protest in response to what they called a lack of transparency House Republicans stormed the National Statuary Hall Thursday demanding to be allowed inside Elijah Cummings casket As voting members of Congress, we have an obligation to our constituents to get inside and find out what’s in there—it could be anything said Matt Gaetz (R-FL) who explained how a closed-casket viewing went against the very foundations of American democracy while House Minority Whip Steve Scalise (R-LA) and Steve King (R-IA) furiously pounded their fists against the coffin Right now it’s an all-Democratic casket Not even the press are allowed inside We’ve been knocking all morning and have yet to receive a response those cowards At press time freaked-out House Republicans were calling for a counter investigation after discovering a body inside the casket',
    'url2': #abstract of a paper re California fires
        '''In this paper we share our approach to real-time segmentation of fire perimeter
from aerial full-motion infrared video we start by describing the problem from a
humanitarian aid and disaster response perspective specifically we explain the
importance of the problem how it is currently resolved and how our machine
learning approach improves it to test our models we annotate a large-scale dataset
of 400000 frames with guidance from domain experts finally we share our
approach currently deployed in production with inference speed of 20 frames per
second and an accuracy of 92'''
}

#in real usage, backend would call this function, then serialize output into json
print(orchestrate(example_usage))