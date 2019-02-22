# platinumrift2solution
Solution for  https://www.codingame.com/ide/puzzle/platinum-rift-episode-2

# Strategy
- Using this strategy, the pods will go to the most favorable zone. 
- The program will attempt to capture as much zone as possible and collect as much platinum as possible.
  Thus, the pods will most likely go to neutral or enemy zones, even more if said zones have platinum sources.
- If the pods encounter enemy pods in an adjacent zones, they will chase if they outnumber the enemies and
  run away if they are outnumbered.
- If pods have visited a zone recently, they won't return to that zone for 3-5 turns.
  
