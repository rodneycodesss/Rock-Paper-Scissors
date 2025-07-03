import random
import os
import time
from typing import Tuple, Dict
import winsound 

class RockPaperScissors:
    def __init__(self):
        self.choices = {
            '1': 'rock',
            '2': 'paper', 
            '3': 'scissors'
        }
        self.choice_symbols = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.difficulty = 'normal'  # easy, normal, hard
        self.streak_count = 0
        self.best_streak = 0
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_banner(self):
        """Display the game banner"""
        print("=" * 50)
        print("🎮 ROCK PAPER SCISSORS CHAMPIONSHIP 🎮")
        print("=" * 50)
        print()
        
    def display_rules(self):
        """Display game rules"""
        print("📋 GAME RULES:")
        print("   🪨 Rock crushes Scissors")
        print("   📄 Paper covers Rock")
        print("   ✂️  Scissors cuts Paper")
        print()
        
    def display_score(self):
        """Display current score"""
        print(f"📊 SCORE - You: {self.player_score} | Computer: {self.computer_score} | Rounds: {self.rounds_played}")
        print("-" * 50)
        
    def get_player_choice(self) -> str:
        """Get and validate player choice"""
        while True:
            print("Choose your weapon:")
            print("1. 🪨 Rock")
            print("2. 📄 Paper")
            print("3. ✂️  Scissors")
            print("4. 📊 View Stats")
            print("5. 🚪 Quit Game")
            print()
            
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice in ['1', '2', '3']:
                return self.choices[choice]
            elif choice == '4':
                self.display_detailed_stats()
                continue
            elif choice == '5':
                return 'quit'
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")
                time.sleep(1)
                continue
                
    def get_computer_choice(self) -> str:
        """Generate random computer choice"""
        return random.choice(list(self.choices.values()))
        
    def determine_winner(self, player_choice: str, computer_choice: str) -> str:
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return 'tie'
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            return 'player'
        else:
            return 'computer'
            
    def display_choices(self, player_choice: str, computer_choice: str):
        """Display both choices with animation"""
        print("🎯 BATTLE TIME!")
        print()
        
        # Countdown animation
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(0.8)
            
        print("   SHOOT! 🎯")
        print()
        
        # Display choices
        player_symbol = self.choice_symbols[player_choice]
        computer_symbol = self.choice_symbols[computer_choice]
        
        print(f"   You chose:      {player_symbol} {player_choice.upper()}")
        print(f"   Computer chose:  {computer_symbol} {computer_choice.upper()}")
        print()
        
    def display_round_result(self, result: str):
        """Display the result of the round"""
        if result == 'player':
            print("🎉 YOU WIN THIS ROUND! 🎉")
            self.player_score += 1
            self.streak_count += 1
            self.best_streak = max(self.best_streak, self.streak_count)
            # winsound.Beep(800, 200)  # Victory sound (uncomment to enable)
        elif result == 'computer':
            print("💻 COMPUTER WINS THIS ROUND! 💻")
            self.computer_score += 1
            self.streak_count = 0  # Reset streak on loss
            # winsound.Beep(400, 300)  # Loss sound (uncomment to enable)
        else:
            print("🤝 IT'S A TIE! 🤝")
            self.streak_count = 0  # Reset streak on tie
            # winsound.Beep(600, 150)  # Tie sound (uncomment to enable)
            
        self.rounds_played += 1
        print()
        
    def display_detailed_stats(self):
        """Display detailed game statistics"""
        print("\n" + "=" * 30)
        print("📈 DETAILED STATISTICS")
        print("=" * 30)
        print(f"Rounds Played: {self.rounds_played}")
        print(f"Your Wins: {self.player_score}")
        print(f"Computer Wins: {self.computer_score}")
        print(f"Ties: {self.rounds_played - self.player_score - self.computer_score}")
        print(f"Best Win Streak: {self.best_streak}")
        
        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            print(f"Your Win Rate: {win_rate:.1f}%")
            
        print("=" * 30)
        input("\nPress Enter to continue...")
        
    def display_final_stats(self):
        """Display final game statistics"""
        self.clear_screen()
        self.display_banner()
        
        print("🏆 FINAL RESULTS 🏆")
        print("=" * 30)
        print(f"Total Rounds: {self.rounds_played}")
        print(f"Your Wins: {self.player_score}")
        print(f"Computer Wins: {self.computer_score}")
        print(f"Ties: {self.rounds_played - self.player_score - self.computer_score}")
        
        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            print(f"Your Win Rate: {win_rate:.1f}%")
            
            if self.player_score > self.computer_score:
                print("\n🎉 CONGRATULATIONS! YOU'RE THE CHAMPION! 🎉")
            elif self.computer_score > self.player_score:
                print("\n💻 Computer wins the championship! Better luck next time!")
            else:
                print("\n🤝 It's a tie! Great match!")
        
        print("\n" + "=" * 30)
        print("Thanks for playing! 👋")
        
    def play_round(self) -> bool:
        """Play a single round. Returns True to continue, False to quit"""
        self.clear_screen()
        self.display_banner()
        self.display_score()
        
        # Get player choice
        player_choice = self.get_player_choice()
        if player_choice == 'quit':
            return False
            
        # Get computer choice
        computer_choice = self.get_computer_choice()
        
        # Display choices with animation
        self.display_choices(player_choice, computer_choice)
        
        # Determine and display result
        result = self.determine_winner(player_choice, computer_choice)
        self.display_round_result(result)
        
        # Pause before next round
        input("Press Enter for next round...")
        return True
        
    def play_game(self):
        """Main game loop"""
        self.clear_screen()
        self.display_banner()
        self.display_rules()
        
        print("🎮 Welcome to Rock Paper Scissors Championship!")
        print("Play as many rounds as you like. Good luck!")
        input("\nPress Enter to start...")
        
        # Main game loop
        while True:
            if not self.play_round():
                break
                
        # Display final statistics
        self.display_final_stats()

def main():
    """Main function to run the game"""
    try:
        game = RockPaperScissors()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\n🛑 Game interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")

if __name__ == "__main__":
    main()