const year = document.getElementById("year");
if (year) year.textContent = String(new Date().getFullYear());

const form = document.getElementById("contact-form");
const status = document.getElementById("form-status");

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!status) return;

  status.textContent = "Sending…";
  const data = Object.fromEntries(new FormData(form).entries());

  try {
    const res = await fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error(`Request failed (${res.status})`);
    const json = await res.json();
    status.textContent = json.message || "Sent.";
    form.reset();
  } catch (err) {
    status.textContent = "Could not send — is Docker running?";
    console.error(err);
  }
});

const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    }
  },
  { threshold: 0.18 }
);

document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
