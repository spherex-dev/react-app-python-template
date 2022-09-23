export async function hello() {
  return fetch("api/hello/hello").then((response) => response.json());
}

export async function greeting(greeting) {
  return fetch(`api/hello/greeting/${greeting}`).then((response) =>
    response.json()
  );
}

export async function echo_post(info) {
  return fetch("api/hello/echo_post", {
    method: "POST",
    body: JSON.stringify(info),
    headers: { "Content-Type": "application/json" },
    // when doing POSTS to cookie authenticated urls
    // for testing, credentials: "included" is needed
    // for tests to pass
    // credentials: "include"
  }).then((response) => response.json());
}
