document.addEventListener("DOMContentLoaded", function () {

    /*
    ========================================
    Search Form
    ========================================
    */

    const searchForm = document.querySelector(".search-form");

    if (searchForm) {

        const searchInput = searchForm.querySelector("input");

        searchInput.addEventListener("keydown", function (event) {

            if (event.key === "Enter") {
                searchForm.submit();
            }

        });

    }


    /*
    ========================================
    Python Jobs Filter
    ========================================
    */

    const pythonCheckbox =
        document.querySelector(
            'input[name="python_only"]'
        );

    if (pythonCheckbox) {

        pythonCheckbox.addEventListener(
            "change",
            function () {

                const form =
                    pythonCheckbox.closest("form");

                if (form) {
                    form.submit();
                }

            }
        );

    }


    /*
    ========================================
    Job Card Animation
    ========================================
    */

    const jobCards =
        document.querySelectorAll(".job-card");

    jobCards.forEach(function (card, index) {

        card.style.opacity = "0";
        card.style.transform = "translateY(10px)";

        setTimeout(function () {

            card.style.transition =
                "opacity 0.35s ease, transform 0.35s ease";

            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, index * 40);

    });


    /*
    ========================================
    External Links
    ========================================
    */

    const externalLinks =
        document.querySelectorAll(
            'a[target="_blank"]'
        );

    externalLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            console.log(
                "Opening external job listing:"
                + " "
                + link.href
            );

        });

    });

});