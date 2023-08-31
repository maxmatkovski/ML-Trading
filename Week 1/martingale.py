""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt 
		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "maxmatkovski3"  # replace tb34 with your Georgia Tech username.  		  	   		  		 		  		  		    	 		 		   		 		 
  		  	   		  		 		  		  		    	 		 		   		 		     		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 900897987  # replace with your GT ID number  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  				 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
def simulate_episode(target_winnings=80, max_loss=-256, win_prob=18/38):
    episode_winnings = 0
    bankroll = 256  # Initial bankroll
    num_bets = 0
    winnings_over_time = []  # Initialize an empty list to keep track of winnings over time

    while target_winnings > episode_winnings > max_loss and num_bets < 1000:
        won = False
        bet_amount = 1
        while not won and num_bets < 1000:
            # Make sure not to bet more than what's left in the bankroll
            bet_amount = min(bet_amount, bankroll)
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bankroll += bet_amount
            else:
                episode_winnings -= bet_amount
                bankroll -= bet_amount
                bet_amount *= 2  # Double the bet for the next round
            num_bets += 1

            # Append the current winnings to the list
            winnings_over_time.append(episode_winnings)

    # Filling the data forward with the last value
    winnings_over_time += [episode_winnings] * (1000 - len(winnings_over_time))

    return winnings_over_time  # Return the winnings over time as a list

def test_code():
    win_prob = 18/38  # American roulette wheel
    np.random.seed(42)
    num_episodes = 1000
    max_spins = 1000  # Maximum number of spins per episode

    # Initialize a 2D array to store the winnings for each spin for each episode
    all_winnings = np.zeros((num_episodes, max_spins))

    for i in range(num_episodes):
        winnings = simulate_episode(target_winnings=80, max_loss=-256, win_prob=win_prob)
        all_winnings[i, :len(winnings)] = winnings

    # Calculate the median and standard deviation of winnings at each spin
    median_winnings = np.median(all_winnings, axis=0)
    std_winnings = np.std(all_winnings, axis=0)

    # Plotting for median
    plt.figure(figsize=(10, 6))
    plt.plot(median_winnings, label="Median Winnings")
    plt.plot(median_winnings + std_winnings, label="Median + 1 Std Dev", linestyle="--")
    plt.plot(median_winnings - std_winnings, label="Median - 1 Std Dev", linestyle="--")

    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.xlabel('Spin Number')
    plt.ylabel('Winnings')
    plt.title('Figure 5: Median and Std Dev of Winnings Over 1000 Episodes with $256 Bankroll')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_code()
    