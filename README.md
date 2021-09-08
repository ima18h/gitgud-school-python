# Project 0
First project in IN1910 about testing with pytest and git

- Repo url : https://github.uio.no/IN1910/H21_project0_imadha.git


## Lessons Learned
- Learned how git can be used to keep things organized, and for potential cooperation. 
- Learned about ways to make testing clean using pytest. 
- Testing can be used as a development strategy. Tests are written first, then the functions are implemented. 


## Notes
I dont think it was needed to define a function for each test. I have all asserts for a certain function inside one defined test function. 
I know it can be better to not do that. 
Nevermind, we using parametrized tests for that now. cool, cool. 

jeg får ikke disse testene til å bestå på sin() funksjonen (opg.8): 
 -    assert sin(pi/4) == pytest.approx(1/sqrt(2))
 -    assert sin(pi/2) == pytest.approx(1)
 -    assert sin(3*pi/2) == pytest.approx(-1),
de bestod før, men ikke under parametrized. 

det er tungvint å lese dette her uten å bruke mange linjer nedover når man bruker parametrized.

jeg får også melding noen ganger om "Test result not found for: ./test_calculator.py::test_sin[0.0-output0]" fra pytest. lite hjelpsom melding... den kommer når jeg prøver å legge til en test til sin funksjonen, men ikke alltid? 

jeg legger til en test, den består. jeg legger til en test til, den feiler. jeg fjerner den siste testen, og nå feiler den første også. fuck. 

Forget all that... fixed it lol, my bad. 


## Authors
- Imad H. (imadha@mail.uio.no)


## Acknowledgements
 - [Readme templates](https://readme.so/)
 - [gitignore tool](gitignore.io)
