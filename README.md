Requirements for running:
- docker (compose is built in to docker, docker-compose not required)
- git
- virtualbox
- vagrant

Vagrant and virtualbox are technically not required, but make standardized development and testing environments much easier to manage. 


How to run:

First, clone this repository locally git@github.com:ag0r/visonTest.git. If you don't have ssh keys set up in your github account, you can instead use https://github.com/ag0r/visonTest.git

now from the root directory execute the command `vagrant up`. This can take several minutes, as it is building and configuring an ubuntu virtual machine.

Once this command completes, you can run `vagrant ssh` to access the virtual machine. On this machine, `/vagrant` is a mount of the repositorys root directory. this is beneficial as the files can be worked on locally and will be synced automatically to the development/test device.

Now you can `cd /vagrant` and execute `docker compose up -d` which will start each component necessary for the application to function. Once this command completes from a web browser on your local machine you should be able to access `http://localhost:3000` and interact with the application as expected.
