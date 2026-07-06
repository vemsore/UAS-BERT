<?php

require_once "helper.php";

/* ==========================================================
LOAD
========================================================== */

$dataset = loadDataset();

$progress = loadProgress();

/* ==========================================================
PAGE
========================================================== */

$page = isset($_POST["page"])
    ? intval($_POST["page"])
    : 1;

$progress["last_page"] = $page;

$progress["updated_at"] = date("Y-m-d H:i:s");

/* ==========================================================
SAVE REVIEW
========================================================== */

if(isset($_POST["id"])){

    foreach($_POST["id"] as $id){

        $field = "label".$id;

        if(!isset($_POST[$field]))
            continue;

        $label = $_POST[$field];

        $progress["review"][$id] = [

            "label" => $label,

            "suggestion" =>
                $dataset[$id]["suggestion"],

            "confidence" =>
                $dataset[$id]["confidence"],

            "need_review" =>
                $dataset[$id]["need_review"],

            "updated_at" =>
                date("Y-m-d H:i:s")

        ];

    }

}

/* ==========================================================
SAVE JSON
========================================================== */

saveProgress($progress);

/* ==========================================================
NEXT PAGE
========================================================== */

header(

"Location:index.php?page=".($page+1)

);

exit;