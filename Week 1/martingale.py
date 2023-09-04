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

# FUNCTION TO SIMULATE AN EPISODE WITH UNLIMITED BANKROLL
def simulate_episode_unlimited(target_winnings=80, max_loss=-256, win_prob=18/38):
    episode_winnings = 0
    num_bets = 0
    winnings_over_time = np.zeros(1000)  # Initialize a NumPy array with 1000 zeros
    while target_winnings > episode_winnings > max_loss and num_bets < 1000:
        won = False
        bet_amount = 1
        while not won and num_bets < 1000:
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2  # double the bet amount
            winnings_over_time[num_bets] = episode_winnings
            num_bets += 1
    return winnings_over_time[:num_bets]

# CODE TO SIMULATE ROULLETTE WITH A LIMITED BANKROLL OF $256
def simulate_episode_limited(target_winnings=80, max_loss=-256, win_prob=18/38):
    episode_winnings = 0
    bankroll = 256  # initial bankroll
    num_bets = 0
    winnings_over_time = np.zeros(1000)
    while episode_winnings < target_winnings and num_bets < 1000:
        if episode_winnings <= max_loss:  # Stop if reached the maximum loss
            winnings_over_time[num_bets:] = max_loss
            break
        won = False
        bet_amount = 1
        while not won and num_bets < 1000:
            bet_amount = min(bet_amount, bankroll)  # Can't bet more than what you have
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                bankroll += bet_amount
            else:
                episode_winnings -= bet_amount
                bankroll -= bet_amount
                bet_amount *= 2
            winnings_over_time[num_bets] = episode_winnings
            num_bets += 1
            if bankroll == 0:  # out of money, stop the episode
                winnings_over_time[num_bets:] = max_loss
                return winnings_over_time[:num_bets + 1]
    return winnings_over_time[:num_bets]

# CODE TO CREATE FIGURE 1
def test_code_fig1():
    actual_win_prob = 18/38  
    np.random.seed(gtid())
    episodes_winnings = [] 
    total_episodes = 10
    for _ in range(total_episodes):
        winnings = simulate_episode_unlimited(win_prob=actual_win_prob)
        episodes_winnings.append(winnings)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    for i, winnings in enumerate(episodes_winnings):
        plt.plot(winnings[:301], label=f"Episode {i+1}")
    plt.xlabel("Bets")
    plt.ylabel("Winnings")
    plt.title("Winnings Over 10 Episodes")
    plt.xlim(0, 300) 
    plt.ylim(-256, 100) 
    plt.legend(loc="upper left") 
    plt.grid(True) 
    plt.show()

#  CODE TO CREATE FIGURE 2
def test_code_fig2():
    actual_win_prob = 18/38
    np.random.seed(gtid())
    total_episodes = 1000
    max_rounds = 1000 
    all_winnings = np.zeros((total_episodes, max_rounds))
    for i in range(total_episodes):
        winnings = simulate_episode_unlimited(win_prob=actual_win_prob)
        fill_values = np.full(max_rounds - len(winnings), winnings[-1])
        winnings = np.concatenate((winnings, fill_values))
        all_winnings[i, :] = winnings
    
    # Calculate the mean and std for each round across all episodes
    mean_winnings = np.mean(all_winnings, axis=0)
    std_winnings = np.std(all_winnings, axis=0)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(mean_winnings[:301], label="Mean Winnings")
    plt.plot(mean_winnings[:301] + std_winnings[:301], label="Mean + 1 Std Dev", linestyle="--")
    plt.plot(mean_winnings[:301] - std_winnings[:301], label="Mean - 1 Std Dev", linestyle="--")
    plt.xlabel("Bets")
    plt.ylabel("Winnings")
    plt.title("Mean Winnings Over 1000 Episodes")
    plt.xlim(0, 300) 
    plt.ylim(-256, 100) 
    plt.legend(loc="upper left") 
    plt.grid(True)
    plt.show()

def test_code_fig3():
    actual_win_prob = 18/38 
    np.random.seed(gtid())
    total_episodes = 1000
    max_rounds = 1000 
    all_winnings = np.zeros((total_episodes, max_rounds))
    for i in range(total_episodes):
        winnings = simulate_episode_unlimited(win_prob=actual_win_prob)
        fill_values = np.full(max_rounds - len(winnings), winnings[-1])
        winnings = np.concatenate((winnings, fill_values))
        all_winnings[i, :] = winnings
    
    # Calculate the median and std for each round across all episodes
    median_winnings = np.median(all_winnings, axis=0)
    std_winnings = np.std(all_winnings, axis=0)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(median_winnings[:301], label="Median Winnings")
    plt.plot(median_winnings[:301] + std_winnings[:301], label="Median + 1 Std Dev", linestyle="--")
    plt.plot(median_winnings[:301] - std_winnings[:301], label="Median - 1 Std Dev", linestyle="--")
    plt.xlabel("Bets")
    plt.ylabel("Winnings")
    plt.title("Median Winnings Over 1000 Episodes")
    plt.xlim(0, 300) 
    plt.ylim(-256, 100) 
    plt.legend(loc="upper left") 
    plt.grid(True) 
    plt.show()
    
# FUNCTION TO CREATE FIGURE 4
def test_code_fig4():
    num_episodes = 1000
    max_spins = 1000
    all_winnings = np.zeros((num_episodes, max_spins))
    # Run the simulation 1000 times
    for i in range(num_episodes):
        episode_winnings = simulate_episode_limited()
        all_winnings[i, :len(episode_winnings)] = episode_winnings
        if len(episode_winnings) < max_spins:
            all_winnings[i, len(episode_winnings):] = episode_winnings[-1] 

    # Calculate the mean and standard deviation at each spin
    mean_winnings = np.mean(all_winnings, axis=0)
    std_winnings = np.std(all_winnings, axis=0)

    # Plot the figure
    plt.figure(figsize=(10, 6))
    plt.plot(mean_winnings, label='Mean Winnings')
    plt.plot(mean_winnings + std_winnings, label='Mean + 1 std', linestyle='--')
    plt.plot(mean_winnings - std_winnings, label='Mean - 1 std', linestyle='--')
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.title('Figure 4: Mean Winnings Over Time (Limited Bankroll)')
    plt.legend()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.grid(True)
    plt.show()

def test_code_fig5():
    num_episodes = 1000
    max_spins = 1000
    all_winnings = np.zeros((num_episodes, max_spins))

    # Run the simulation 1000 times
    for i in range(num_episodes):
        episode_winnings = simulate_episode_limited()
        all_winnings[i, :len(episode_winnings)] = episode_winnings
        if len(episode_winnings) < max_spins:
            all_winnings[i, len(episode_winnings):] = episode_winnings[-1] 

    # Calculate the median and standard deviation at each spin
    median_winnings = np.median(all_winnings, axis=0)
    std_winnings = np.std(all_winnings, axis=0)

    # Plot the figure
    plt.figure(figsize=(10, 6))
    plt.plot(median_winnings, label='Median Winnings')
    plt.plot(median_winnings + std_winnings, label='Median + 1 std', linestyle='--')
    plt.plot(median_winnings - std_winnings, label='Median - 1 std', linestyle='--')
    plt.xlabel('Spins')
    plt.ylabel('Winnings')
    plt.title('Figure 5: Median Winnings Over Time (Limited Bankroll)')
    plt.legend()
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.grid(True)
    plt.show()



if __name__ == "__main__":

# Figure 1
    test_code_fig1()

# Figure 2
    test_code_fig2()

# Figure 3
    test_code_fig3()

# Figure 4
    test_code_fig4()

# Figure 5
    test_code_fig5()





