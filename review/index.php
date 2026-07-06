<?php

require_once "helper.php";

$dataset = loadDataset();

$progress = loadProgress();

/* ============================================
PAGE
============================================ */

$perPage = 20;

$page = isset($_GET["page"])
    ? intval($_GET["page"])
    : $progress["last_page"];

$totalPage = totalPage(
    $dataset,
    $perPage
);

if($page < 1)
    $page = 1;

if($page > $totalPage)
    $page = $totalPage;

$data = getPageData(
    $dataset,
    $page,
    $perPage
);
/*
echo "<pre>";
print_r(array_keys($data[0]));
echo "</pre>";
exit;
*/
$start = ($page-1)*$perPage;

?>
<!DOCTYPE html>

<html lang="id">

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width,initial-scale=1">

<title>

Smart Labeling Dashboard

</title>

<link
href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
rel="stylesheet">

<link
href="assets/style.css"
rel="stylesheet">

</head>

<body>

<div class="container py-4">

<div class="card shadow">

<div class="card-header bg-primary text-white">

<h3>

Smart Labeling Review

</h3>

</div>

<div class="card-body">

<!-- Progress -->

<div class="mb-4">

<h5>

Progress Review

</h5>

<?php

$percent = progressPercent(
    $dataset,
    $progress
);

?>

<div class="progress">

<div

class="progress-bar bg-success"

style="width:<?= $percent ?>%">

<?= $percent ?> %

</div>

</div>

<p class="mt-2">

<?= reviewedCount($progress) ?>

/

<?= count($dataset) ?>

Sudah Direview

</p>

</div>

<form

method="POST"

action="save.php">

<input

type="hidden"

name="page"

value="<?= $page ?>">

<table

class="table table-bordered table-hover align-middle">

<thead class="table-dark">

<tr>

<th width="4%">

No

</th>

<th>

Tweet

</th>

<th width="10%">

Suggestion

</th>

<th width="8%">

Conf.

</th>

<th width="18%">

Final Label

</th>

</tr>

</thead>

<tbody>

<?php

foreach($data as $i=>$row):

$index = $start+$i;

$current =

isset($progress["review"][$index])

?

$progress["review"][$index]["label"]

:

($row["final_label"]=="" ?

$row["suggestion"]

:

$row["final_label"]);

?>

<tr>

<td>

<?= $index+1 ?>

</td>

<td>

<?= nl2br(htmlspecialchars(getTweet($row))) ?>

<br><br>

<small class="text-muted">

Positive :

<?= htmlspecialchars($row["positive_words"]) ?>

<br>

Negative :

<?= htmlspecialchars($row["negative_words"]) ?>

<br>

Policy :

<?= htmlspecialchars($row["policy_words"]) ?>

</small>

</td>

<td>

<span

class="badge bg-<?= badgeColor($row["suggestion"]) ?>">

<?= $row["suggestion"] ?>

</span>

</td>

<td>

<?= round($row["confidence"]*100,1) ?> %

</td>

<td>

<input
type="hidden"
name="id[]"
value="<?= $index ?>">

<div class="form-check">

<input

class="form-check-input"

type="radio"

name="label<?= $index ?>"

value="positive"

<?= $current=="positive"?"checked":"" ?>

>

Positive

</div>

<div class="form-check">

<input

class="form-check-input"

type="radio"

name="label<?= $index ?>"

value="neutral"

<?= $current=="neutral"?"checked":"" ?>

>

Neutral

</div>

<div class="form-check">

<input

class="form-check-input"

type="radio"

name="label<?= $index ?>"

value="negative"

<?= $current=="negative"?"checked":"" ?>

>

Negative

</div>

</td>

</tr>

<?php endforeach; ?>

</tbody>

</table>

<div class="d-flex justify-content-between">

<a

class="btn btn-secondary"

href="?page=<?= max(1,$page-1) ?>">

Previous

</a>

<button

class="btn btn-primary">

💾 Simpan Halaman

</button>

<a

class="btn btn-secondary"

href="?page=<?= min($totalPage,$page+1) ?>">

Next

</a>

</div>

</form>

</div>

</div>

</div>

</body>

</html>