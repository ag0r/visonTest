Requirements for running:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [vagrant](https://www.virtualbox.org/wiki/Downloads)
- [docker](https://docs.docker.com/get-docker/) (compose is built in to docker, docker-compose not required) IF vagrant is not used

Vagrant and virtualbox are technically not required, but make standardized development and testing environments much easier to manage and remove the requirement for docker to be installed locally.


How to run:

First, clone this repository locally git@github.com:ag0r/visonTest.git. If you don't have ssh keys set up in your github account, you can instead use https://github.com/ag0r/visonTest.git

now from the root directory execute the command `vagrant plugin install vagrant-docker-compose` to install the docker compose plugin. From here you're ready to go ahead and `vagrant up`. This can take several minutes, as it is building and configuring an ubuntu virtual machine.

Once this command completes, you can run `vagrant ssh` to access the virtual machine. On this machine, `/vagrant` is a mount of the repositorys root directory. this is beneficial as the files can be worked on locally and will be synced automatically to the development/test device.

Now you can `cd /vagrant` and execute `docker compose up -d` which will start each component necessary for the application to function. Once this command completes from a web browser on your local machine you should be able to access `http://localhost:3000` and interact with the application as expected. 

to execute tests, simply run `./flask/execute_tests.sh`
