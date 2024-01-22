# <span style="color:blue">Motivation/Background Material</span>



Game theory is the mathematical study of strategic decision-making, in which the
outcome of a decision depends not only on one’s choices but also on the choices of others. The
game theory contains an important concept which is the concept of Nash Equilibrium. We have
looked at various coordination games, and we have analyzed the static dynamics of these games.
By this, I mean figuring out the pure strategy and the mixed strategy Nash equilibrium. Now we
want to understand how different strategies evolve and persist over time, in a population of
individuals. Essentially, we want to study the evolutionary dynamics of a game, to understand
not only the mathematical analysis of strategic decision-making but also the evolutionary factor.
This leads us to the study of evolutionary game theory.
An Important concept of evolutionary game theory is finding the evolutionarily stable
strategy(ESS), if present. An evolutionarily stable strategy is a strategy within a game that is
impermeable when adopted by a population and will remain dominant even in the presence of
other strategies. This concept is the center of evolutionary game theory because ESS can provide
insight into how strategies within a game will evolve and interact in a population over time. It
will also allow us to make predictions about the long-term outcomes of different games.
Furthermore, this will give us insight into how strategies within a game will be favored by
natural selection over time, and how cooperation and altruism emerge and be sustained in a
population.
Lastly, we want to discover whether game models are more likely to converge to a payoff
or risk-dominant strategy. Even to this day, there exists the debate believing that a
group of people playing a game will more likely choose the payoff-dominant strategy than a risk--
dominant strategy. It is assumed that people are braver to betting higher than playing with a
risky mentality. We will discover more about this in the scientific paper “Risk Dominance and
Coordination Failures in Static Games” by Paul G. Straub. This will illustrate if people play a
game with a mentality of not wanting to risk it all or if people are more willing to aim higher and
put everything on the line.




# <span style="color:blue">Probelm Statment</span>


We will analyze and compare the evolutionary dynamics of a least 4 games which are the
following: the rock scissors paper game, the chicken game, the stag hunt game, and the battle of
the sexes games. A quick description of each game, the rock scissors paper game, it’s a game
played by two players using their hands to form one of three shapes: a rock, paper, or scissors.
The objective of the game is for each player to select one of the three options, and the winner is
determined by the game rules. Rock beats scissors, scissors beat paper, and paper beats rock. The
chicken game, this game consists of two people Player 1 and Player 2. Each Player will position
their cars on the opposite sides of a one-way street, where the front of their cars will point
directly at each other. Then, both players will step on the accelerator, and drive right at each
other. Right before colliding, both players will simultaneously have to decide whether they want
to keep driving or swerves off the street. Whoever swerve is considered the chicken. The battle
of sexes game is a game that consists of two players, who must choose between two
options/strategies: attending a ballet event or attending a football game. They both want to attend
the same event but don’t have any sort of communication. The stag hunt game is a two-player
game that must choose between cooperating to hunt a stag or acting independently to hunt a
rabbit.
Hence, to analyze the evolutionary dynamics we need a model that conducts the
evolutionary game theory algorithm, shown in Figure 1. In short, the evolutionary game theory
algorithm is when you have a population of individuals who play a game in pairs, and the game
has unique rules and payoffs structure. After they have finished playing the game, they will
receive a reward. Then they compare their reward with a randomly selected individual from the
population. If the random individual had a better payoff/reward, then they copy that behavior.
Then the population is updated and we repeat the same procedure for numerous iterations.
Essentially, it is the same concept in the evolutionary algorithm, but these game rules take the
place of the fitness function. Having a model that conducts the evolutionary game theory
algorithm, we need to analyze whether all four games have an evolutionarily stable strategy
despite each game having a unique payoff structure and game dynamics. Also, keep in mind,
“strategies are not assumed to be selected by players but rather hardwired into the individual’s
genetic makeup”(Dr.Thanos). This is an important factor to take into consideration when
planning out the model, as this determines the evolutionary aspect when running each game in
the model. Do you think that each game will have an evolutionarily stable strategy when each
game is run for a period of time?
Lastly, visualize that you are playing the stag hunt game with another random player.
Now take into consideration the payoff structure for the stag hunt game, which is illustrated in
Figure 2. If you were to play this game for n number of periods, are you more likely to choose
the stag strategy or the rabbit strategy? Hence, player 2 will choose randomly and you don’t
know his incentives, he might play it safe and choose the rabbit strategy. Keep in mind that if
you and Player 2, choose different strategies, then you or Player 2 will receive a payoff of zero
and the other gets a payoff of 1. Do you think that both you and Player 2 will go for the greater
payoff which is the stag strategy and is also known as the payoff dominant strategy? Or do you
think that both you and player 2 will go for the rabbit strategy which has the highest minimal
payoff and is known as the risk-dominant strategy? Also, put yourself as the spectator do you
think this game model will converge to a payoff-dominant strategy or risk-dominant strategy?
