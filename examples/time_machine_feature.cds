time_machine_on(5); // Keep last 5 snapshots

counter = 0;
likho("Initial counter: ", counter);

counter = 1;
likho("Counter after first change: ", counter);

counter = 2;
likho("Counter after second change: ", counter);

peeche(1); // Go back 1 step
likho("Counter after going back: ", counter);

timeline(); // Show all snapshots
