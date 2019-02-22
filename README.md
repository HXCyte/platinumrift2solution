# platinumrift2solution
Solution for  https://www.codingame.com/ide/puzzle/platinum-rift-episode-2

# Strategy
- Using this strategy, the pods will go to the most favorable adjacent zone. favorable zones are either zones with platinum sources,
  neutral zones, enemy zones, zones  with outnumbered enemy pods, or zones which have not been visited recently.
- The program will attempt to capture as much zone as possible and collect as much platinum as possible.
  Thus, the pods will most likely go to neutral or enemy zones, even more if said zones have platinum sources.
- If the pods encounter enemy pods in an adjacent zones, they will chase if they outnumber the enemies and
  run away if they are outnumbered.
- If pods have visited a zone recently, they won't return to that zone for 3-5 turns.
- If pods find out the enemy base and are prepared, they will attack it!
- Criterias listed above have their own weight in the calculation, so some conditions are more favorable than the other.
  For example, zones with five platinum sources are mor favorable than zones with only one source.
- If one zone contains more than 20 pods, there will be a chance that the pods split into two teams and
  act independently.
- Just to be safe, a good amount of pods will be kept in base as guards.
  
  

16518230-16518331-19918165-16718288
