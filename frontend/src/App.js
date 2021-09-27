import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "algorithm";
import { Counter, Home, Navigation } from "common";
import { Linear, Mathmatics, Nonlinear } from "datastructure";
import React from "react";
import { Route, Switch, Redirect } from 'react-router-dom';

const App = () => (
  <>
  <Navigation />
  <Switch>
  <Route  exact path= '/' component = {Home}/>
  <Redirect  from = '/home' to = {'/'}/>
  <Route  exact path= '/counter' component = {Counter}/>
  <Route  exact path= '/math' component = {Mathmatics}/>  
  <Route  exact path= '/linear' component = {Linear}/>  
  <Route  exact path= '/nonlinear' component = {Nonlinear}/>  
  <Route  exact path= '/bruteForce' component = {BruteForce}/>  
  <Route  exact path= '/divideConquer' component = {DivideConquer}/>  
  <Route  exact path= '/greedy' component = {Greedy}/>  
  <Route  exact path= '/dynamicP' component = {DynamicProgramming}/>  
  <Route  exact path= '/backTracking' component = {BackTracking}/>  
  </Switch>
  </>
)

export default App