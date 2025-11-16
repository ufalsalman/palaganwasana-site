fetch("/entri/entri.json")
  .then(res => res.json())
  .then(entries => {
    const ul = document.getElementById("daftar-entri");

    entries.forEach(e => {
      const li = document.createElement("li");
      const a = document.createElement("a");

      a.href = "/entri/" + e.file;
      a.textContent = e.title;

      li.appendChild(a);
      ul.appendChild(li);
    });
  })
  .catch(err => {
    console.error("Gagal memuat entri:", err);
  });
