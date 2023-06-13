(async (n) => {
  let validUsers = [];

  await (async () => {
    for (let i = 0; i <= n; i++) {
      await fetch(`https://ark.shcs.nsw.edu.au/search/user/${i}`)
        .then((response) => {
          if (response.ok) {
            validUsers.push(i);
          }
        })
        .catch((error) => console.log(`${error.status}: ${error.statusText}`));
    }
  })();

  console.log(validUsers);
})();
