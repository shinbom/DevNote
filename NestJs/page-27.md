# 관계 설정하기

```typescript
// report.controller.ts
import { Controller, Post, Body, UseGuards } from '@nestjs/common';
import { CreateReportDto } from './dtos/create-report.dto';
import { ReportsService } from './reports.service';
import { AuthGuard } from 'src/guards/auth.guard';
import { CurrentUser } from 'src/users/decorators/current-user.decorator';
import { User } from 'src/users/user.entity';

@Controller('reports')
export class ReportsController {
  constructor (private reposrtService : ReportsService) {}

  @Post()
  @UseGuards(AuthGuard)
  createReport(@Body() body : CreateReportDto, @CurrentUser() user : User) {
    return this.reposrtService.create(body, user)
  }
}
```

`Report 컨트롤러`에 현재 사용자를 찾을 수 있도록 `CurrentUser 데코레이터`와 `User 엔티티`를 가져온다.

```typescript
// report.service.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm/dist/common';
import { Repository } from 'typeorm'
import { Report } from './report.entirty';
import { CreateReportDto } from './dtos/create-report.dto';
import { User } from 'src/users/user.entity';


@Injectable()
export class ReportsService {
  constructor(@InjectRepository(Report) private repo : Repository<Report>) {}

  create (reportDto : CreateReportDto, user : User) {
    const report  = this.repo.create(reportDto);
    report.user = user

    return this.repo.save(report);
  }
}
```

`create`메서드에 user 인자를 추가하여, 조회된 user를 넣을 수 있도록 한다.
